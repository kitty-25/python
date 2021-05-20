#Strong number(sum of cube of its digit)eg:153-->1!+5!+3!

n=int(input("Enter the number:"))

sum=0
temp=n

while n!=0:
    strong=n%10
    n//=10

    fact=1
    for i in range(1,strong+1):
        fact*=i
    sum+=fact
    
print(sum)
        
if(temp==sum):
    print(f"{sum} is a strong number")
else:
    print(f"{sum} is not a strong number")
    

#iteration n%10	 n//=10	  fact		sum
#   1        5	  14	  120	 0+120=120        
#   2        4	   1      24    120+24=144
#   3        1	   0	   1    144+1=145

