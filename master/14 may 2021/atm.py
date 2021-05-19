#process of ATM

amt=20000
pin=int(input("Enter your pin:"))

if(pin == 2345):
    print("Verification Successful")

    option=int(input("Please selsct your option: 1.Withdraw 2.Balance Enquiry 3.Deposit 4.Exit"))
    if(option==1):
        amount=int(input("Please enter your withdrawal amount:"))
        if(amount < amt):
            withdrawal = amt-amount
            print(f"Your current balance is {withdrawal}")
        else:
            print("You have exceeded your balance")
    elif(option==2):
        print(f"Your current balance is {amt}")
    elif(option==3):
        dep=int(input("Please enter your deposit amount:"))
        deposit = amt+dep
        print(f"Your current balance is {deposit}")
    elif(option==4):
        print("Thank you for using ATM")
            
else:
    print("You have entered the wrong pin")

