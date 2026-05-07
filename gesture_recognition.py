"""
Real-Time Hand Gesture Recognition
====================================
Compatible with : mediapipe >= 0.10.21  (new Tasks API)
Tech Stack      : OpenCV + MediaPipe Tasks
Tested on       : mediapipe 0.10.30–0.10.35, Python 3.10–3.12, Windows 11

--- SETUP (run once) ---
    pip install opencv-python mediapipe

--- RUN ---
    python gesture_recognition.py

On first run the script auto-downloads the hand_landmarker.task model
(~9 MB) into the same folder. Subsequent runs use the cached file.

Recognized Gestures
-------------------
  1. Open Palm  – all 5 fingers extended
  2. Fist       – all 5 fingers curled
  3. Peace Sign – index + middle extended, rest curled
  4. Thumbs Up  – only thumb extended
  5. Pointing   – only index extended
"""

import math
import time
import threading
import urllib.request
import os

import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision

# ──────────────────────────────────────────────
# Model download
# ──────────────────────────────────────────────
MODEL_URL  = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
MODEL_PATH = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")

def ensure_model():
    if os.path.exists(MODEL_PATH):
        return
    print(f"[INFO] Downloading hand landmarker model (~9 MB) ...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print(f"[INFO] Model saved to: {MODEL_PATH}")


# ──────────────────────────────────────────────
# Landmark index constants (MediaPipe 21-point model)
# ──────────────────────────────────────────────
WRIST      = 0
THUMB_IP   = 3;  THUMB_TIP  = 4
INDEX_PIP  = 6;  INDEX_TIP  = 8
MIDDLE_PIP = 10; MIDDLE_TIP = 12
RING_PIP   = 14; RING_TIP   = 16
PINKY_PIP  = 18; PINKY_TIP  = 20


# ──────────────────────────────────────────────
# Finger geometry helpers
# ──────────────────────────────────────────────

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def px(lm, idx, w, h):
    """Normalised landmark → integer pixel (x, y)."""
    l = lm[idx]
    return int(l.x * w), int(l.y * h)


def finger_up(lm, tip_idx, pip_idx, w, h):
    """True when TIP is further from wrist than PIP (finger extended)."""
    wrist = px(lm, WRIST, w, h)
    return dist(px(lm, tip_idx, w, h), wrist) > dist(px(lm, pip_idx, w, h), wrist)


def thumb_up(lm, w, h):
    """Thumb uses IP vs TIP distance from wrist (works for both hands)."""
    wrist = px(lm, WRIST, w, h)
    return dist(px(lm, THUMB_TIP, w, h), wrist) > dist(px(lm, THUMB_IP, w, h), wrist)


def finger_states(lm, w, h):
    return {
        "thumb" : thumb_up(lm, w, h),
        "index" : finger_up(lm, INDEX_TIP,  INDEX_PIP,  w, h),
        "middle": finger_up(lm, MIDDLE_TIP, MIDDLE_PIP, w, h),
        "ring"  : finger_up(lm, RING_TIP,   RING_PIP,   w, h),
        "pinky" : finger_up(lm, PINKY_TIP,  PINKY_PIP,  w, h),
    }


# ──────────────────────────────────────────────
# Gesture classification
# ──────────────────────────────────────────────

def classify(fs):
    t, i, m, r, p = fs["thumb"], fs["index"], fs["middle"], fs["ring"], fs["pinky"]
    total = sum([t, i, m, r, p])

    if total == 5:                              return "Open Palm"
    if total == 0:                              return "Fist"
    if i and m and not r and not p:             return "Peace Sign"
    if t and not i and not m and not r and not p: return "Thumbs Up"
    if i and not m and not r and not p:         return "Pointing"
    return "Unknown"


# ──────────────────────────────────────────────
# Drawing
# ──────────────────────────────────────────────
COLORS = {
    "Open Palm" : (50,  220, 120),
    "Fist"      : (60,   80, 230),
    "Peace Sign": (230, 180,  50),
    "Thumbs Up" : (50,  200, 255),
    "Pointing"  : (255, 140,  50),
    "Unknown"   : (160, 160, 160),
}

# MediaPipe drawing helpers
mp_drawing       = mp.solutions.drawing_utils        if hasattr(mp, "solutions") else None
mp_drawing_styles= mp.solutions.drawing_styles       if hasattr(mp, "solutions") else None

# Connections list — same regardless of API version
HAND_CONNECTIONS = mp_vision.HandLandmarker.HAND_CONNECTIONS if hasattr(
    mp_vision.HandLandmarker, "HAND_CONNECTIONS") else None

# Fallback: draw skeleton manually with OpenCV
CONNECTIONS_IDX = [
    (0,1),(1,2),(2,3),(3,4),         # thumb
    (0,5),(5,6),(6,7),(7,8),         # index
    (0,9),(9,10),(10,11),(11,12),    # middle
    (0,13),(13,14),(14,15),(15,16),  # ring
    (0,17),(17,18),(18,19),(19,20),  # pinky
    (5,9),(9,13),(13,17),            # palm
]


def draw_skeleton(frame, lm, w, h, color):
    """Draw hand skeleton using raw OpenCV (no mp.solutions dependency)."""
    for a, b in CONNECTIONS_IDX:
        cv2.line(frame, px(lm, a, w, h), px(lm, b, w, h), (80, 80, 80), 2, cv2.LINE_AA)
    for idx in range(21):
        pt = px(lm, idx, w, h)
        is_tip = idx in (4, 8, 12, 16, 20)
        cv2.circle(frame, pt, 6 if is_tip else 4, color, -1, cv2.LINE_AA)
        cv2.circle(frame, pt, 6 if is_tip else 4, (255, 255, 255), 1, cv2.LINE_AA)


def draw_hud(frame, label, hand_count):
    h, w = frame.shape[:2]
    color = COLORS.get(label, (160, 160, 160))

    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (w - 10, 88), (18, 18, 18), -1, cv2.LINE_AA)
    cv2.addWeighted(overlay, 0.55, frame, 0.45, 0, frame)

    cv2.rectangle(frame, (10, 10), (w - 10, 15), color, -1)
    cv2.putText(frame, label or "No hand detected",
                (24, 68), cv2.FONT_HERSHEY_DUPLEX, 1.5, color, 2, cv2.LINE_AA)

    info = f"Hands: {hand_count}"
    (tw, _), _ = cv2.getTextSize(info, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
    cv2.putText(frame, info, (w - tw - 18, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1, cv2.LINE_AA)

    cv2.rectangle(frame, (0, h - 30), (w, h), (18, 18, 18), -1)
    cv2.putText(frame, "Press Q to quit", (10, h - 9),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (110, 110, 110), 1, cv2.LINE_AA)


# ──────────────────────────────────────────────
# Thread-safe result holder
# (Tasks API in LIVE_STREAM mode calls a callback on a bg thread)
# ──────────────────────────────────────────────
class ResultHolder:
    def __init__(self):
        self._lock   = threading.Lock()
        self._result = None

    def update(self, result):
        with self._lock:
            self._result = result

    def get(self):
        with self._lock:
            return self._result


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def run():
    ensure_model()

    holder = ResultHolder()

    def on_result(result, output_image, timestamp_ms):
        holder.update(result)

    # Build landmarker options
    base_opts = mp_python.BaseOptions(model_asset_path=MODEL_PATH)
    opts = mp_vision.HandLandmarkerOptions(
        base_options=base_opts,
        running_mode=mp_vision.RunningMode.LIVE_STREAM,
        num_hands=2,
        min_hand_detection_confidence=0.6,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
        result_callback=on_result,
    )

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Try VideoCapture(1) or VideoCapture(2).")

    print("[INFO] Webcam opened. Press Q to quit.")

    with mp_vision.HandLandmarker.create_from_options(opts) as landmarker:
        while True:
            ok, frame = cap.read()
            if not ok:
                continue

            frame    = cv2.flip(frame, 1)
            img_h, img_w = frame.shape[:2]

            # Send frame to landmarker (non-blocking)
            rgb       = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image  = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            timestamp = int(time.time() * 1000)
            landmarker.detect_async(mp_image, timestamp)

            # Render latest result (may be one frame behind — acceptable for live preview)
            result = holder.get()
            label      = ""
            hand_count = 0

            if result and result.hand_landmarks:
                hand_count = len(result.hand_landmarks)
                for lm in result.hand_landmarks:
                    color = COLORS.get(label or "Unknown", (160, 160, 160))
                    draw_skeleton(frame, lm, img_w, img_h, color)
                    if not label:
                        fs    = finger_states(lm, img_w, img_h)
                        label = classify(fs)

            draw_hud(frame, label, hand_count)
            cv2.imshow("Hand Gesture Recognition", frame)

            if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Session ended.")


if __name__ == "__main__":
    run()