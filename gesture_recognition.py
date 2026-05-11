first_name = input("Enter Your First Name: ").strip()
last_name = input("Enter Your Last Name: ").strip()

username = first_name.lower() + last_name.lower()

full_name = first_name.title() + " " + last_name.title()

print(f"""
Full Name: {full_name}
Username: {username}
Total Characters: {len(full_name)}
""")