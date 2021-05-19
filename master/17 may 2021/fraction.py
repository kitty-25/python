#1/2+3/2+5/2=?

n=int(input("Enter the number:"))
sum=0.0
for i in range(1,n,2):
    print(i/2,end="+")
    sum+=i/2
print(str(n/2)+"="+str(sum+n/2))


#if n=5
#start  stop  sum+=i/2  result  step
#(n+2)
# 1      5    0+0.5      0.5     1
# 3      5    0.5+1.5     2      3
# 5      5    2+2.5      4.5     5 ---- stop execution


