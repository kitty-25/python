#convert first and last letter in a string
n=input("Enter your string:")
for i in n.split():
    print(i.title()+i[-1].upper())
    
