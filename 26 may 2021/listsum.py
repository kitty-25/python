# sum of first largest and third smallest number

n=[]
size=int(input("Enter the size of the list:"))

for i in range(size):
    num=int(input("Enter the numbers:"))
    n.append(num)
n.sort()
sum=n[-1]+n[2]
print("1st largest+3rd smallest="+str(n[-1])+"+"+str(n[2])+"="+str(sum))
