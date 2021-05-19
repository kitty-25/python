#Amstrong number(sum of cube of its digit)eg:153-->1^3+5^3+3^3
#series any 5-->7, 10, 8, 11, 9, 12, ...
#atm --> card numner verify start and end digit before proceeding for withdraw and deposit

n=int(input("Enter the number:"))
temp=n
amstrong=0

while n!=0:
    amstrong+=(n%10)**3
    n//=10
print(amstrong)

if(temp==amstrong):
    print(f"{temp} is an amstrong number")
else:
    print(f"{temp} is not an amstrong number")
