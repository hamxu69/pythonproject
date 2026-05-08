username = input("Username: ")
password = input("Enter Password: ")
if username == "admin" :
    if password == "1234":
        print('Login Successful')
    else:
        print('Invalid Password')
else:    
    print('Invalid password!')