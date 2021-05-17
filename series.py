#10+8+6+4+2=?

n=int(input("Enter the number:"))
sum=0
for i in range(n,2,-2):
    print(i,end="+")
    sum+=i
print(str(i-2)+"="+str(sum+2))


#if n=10
#start  stop  sum+=i  result  step
#(n-2)
# 10     0    0+10=10   10     10
# 8      0    10+8=18   18      8
# 6      0    18+6=24   24      6
# 4      0    24+4=28   28      4
# 2      0    28+2=30   30      2------ stop execution



