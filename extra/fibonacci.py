#fibonacci series (-1 1 0 1 1 2 3 5 8 13)

n=int(input())

a=-1
b=1

for i in range(n):
    c=a+b
    print(str(c),end=" ")
    a=b
    b=c
    
