n=[]

r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))

for i in range(r):
    n.append([])
    for j in range(c):
        n[i].append(int(input()))
        
for i in range(r):
    for j in range(c):
        if j==0 or i+j==len(n)//2 or i-j==len(n)//2:
            print (n[i][j],end="")
        else:
            print(" ",end="")
    print()
    
