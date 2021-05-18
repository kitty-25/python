#series -->  7, 10, 8, 11, 9, 12,...

n=int(input("Enter the number:"))
print(n,end=",")
for i in range(n):
    c=n+3
    d=c-2
    print(str(c)+","+str(d),end=",")
    n=d
    c=d
    
