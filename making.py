fingers = [0, 1, 1, 0, 0, 0, 1, 1]
count = 0
for finger in fingers :
    if finger == True:
        count += 1
print(f"I am pointing {count} fingers")