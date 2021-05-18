#get first and last digit of the card for verification.
#Then, proceed with withdrawal and deposit

amt=10000

fDigit=int(input("Enter your first digit of your card:"))
lDigit=int(input("Enter your last digit of your card:"))

if(fDigit<=9 and lDigit<=9):
    print("your card number has been validating")
    card=int(input("Enter your card number:"))
    if(card >=1000000000000000 and card <=9999999999999999):
        print("Your account has been verified")
        option=int(input("Please select the following options: 1.Withdrawal 2.Deposit 3.Exit"))
        if(option==1):
            amount=int(input("Please enter your withdrawal amount:"))
            if(amount < amt):
                withdrawal = amt-amount
                print(f"Your current balance is {withdrawal}")
            else:
                print("You have exceeded your balance")
        elif(option==2):
            dep=int(input("Please enter your deposit amount:"))
            deposit = amt+dep
            print(f"Your current balance is {deposit}")
        elif(option==3):
            print("Thank you for using ATM") 
    else:
        print("You account has not been verified")
else:
    print("Invalid digit")



    
