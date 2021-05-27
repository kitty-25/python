# find the difference number of even and odd numbers

n=[]
size=int(input("Enter the size of the list:"))
even=0
odd=0

for i in range(size):
    num=int(input("Enter the numbers:"))
    n.append(num)
    if n[i]%2==0:
        even=even+1
    else:
        odd=odd+1

diff=even-odd
print("even-odd:"+str(even)+"-"+str(odd)+"="+str(diff))
