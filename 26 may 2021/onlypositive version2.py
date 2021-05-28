# program that accept only postive number

n=[]
size=int(input("Enter the size of the list:"))

for i in range(size+1):
    num=int(input("Enter the numbers:"))
    if num>0:
        continue
    else:
        num=int(input("Enter the numbers:"))
