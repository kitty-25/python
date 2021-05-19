#Get 2-digit number from user and cross calculate
#23
#42
#(2+2)+(3+4)=11
n1=int(input("Enter first 2-digit number:"))
n2=int(input("Enter second 2-digit number:"))

digit1=n1//10
digit2=n2%10

ldigit1=n1%10
ldigit2=n2//10

total1=digit1+digit2
total2=ldigit1+ldigit2

final=total1+total2

print(f"{total1}+{total2}={final}")
         

