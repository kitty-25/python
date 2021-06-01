#signup-->name, pwd, confirm pwd, dob, mobile number

print("Welcome to Instagram")
welcome = int(input("Please select 1. New User 2.exit"))
list = []
if(welcome == 1):
    
    print("SIGN UP")
    name=input("Enter your Username/email:")
    dob=input("Enter your DOB:")
    phone=int(input("Enter your Mobile nuber:"))
    password=input("Enter create your password:")
    confirm_password=input("Confirm your password:")
    while password!=confirm_password:
        name=input("Enter your Username/email:")
        dob=int(input("Enter your DOB:"))
        phone=int(input("Enter your Mobile nuber:"))
        password=input("Enter create your password:")
        confirm_password=input("Confirm your password:")
    list.append(name)
    list.append(dob)
    list.append(phone)
    list.append(confirm_password)
    print(list)
    print("You have successfully created an account")

else:
    print("You have exited the page")
