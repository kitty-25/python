#series4 --> 3, 4, 7, 8, 11, 12, ...
#in the form of +1 and +3

n=int(input("Enter the number:"))
print(n,end=",")
for i in range(n):
    c=n+1
    d=c+3
    print(str(c)+","+str(d),end=",")
    n=d
    c=d
