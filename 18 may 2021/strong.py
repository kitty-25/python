#Strong number(sum of cube of its digit)eg:153-->1!+5!+3!

n=int(input("Enter the number:"))

strong=0
fact=1
temp=n

while n!=0:
    strong+=n%10
    n//=10
    
    for i in range(1,n):
        fact*=i

    strong+=fact
    
print(strong)
        
if(temp==strong):
    print(f"{temp} is a strong number")
else:
    print(f"{temp} is not a strong number")
