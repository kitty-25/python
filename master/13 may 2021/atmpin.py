#simulate ATM logic
pin=int(input("Enter your pin:"))

if ((pin>=1000 and pin<=9999) and (pin%10==2 or pin%10==7)):
    print(f"Your pin is {pin}")
else:
    print(f"Invalid pin")
    

