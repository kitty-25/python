#factorial
n=int(input())
fact=1
for i in range(1,n):
    fact*=i
    print(str(i)+"*",end="")
print(str(n)+"="+str(fact*n))
