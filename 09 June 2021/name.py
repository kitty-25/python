#name should be only alphabets
n=input("Enter the name:")
while(True):
    if(n.isalpha()):
        print("Welcome  "+n)
    
    n=input("Enter the name:")
