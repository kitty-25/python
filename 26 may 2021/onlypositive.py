# program that accept only postive number

n=[]
size=int(input("Enter the size of the list:"))

for i in range(size):
    num=int(input("Enter the numbers:"))
    if num<0:
        pos=int(input("please enter positive numbers:"))
