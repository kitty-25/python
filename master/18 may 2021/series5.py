#series5-->31, 29, 24, 22, 17, ...
#in form of -2,-5

n=int(input("Enter the number:"))
print(n,end=",")
for i in range(n):
    c=n-2
    d=c-5
    print(str(c)+","+str(d),end=",")
    n=d
    c=d
