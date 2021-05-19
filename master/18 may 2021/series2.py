#series2 --> 36, 34, 30, 28, 24, ...
#in the form of -2 and -4

n=int(input("Enter the number:"))
print(n,end=",")
for i in range(n):
    c=n-2
    d=c-4
    print(str(c)+","+str(d),end=",")
    n=d
    c=d
