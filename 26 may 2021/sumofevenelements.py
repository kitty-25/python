n=[]
size=int(input("Please enter the list size:"))
res=0

for i in range(size):
    x=int(input("Enter the element:"))
    n.append(x)
    if i%2==0:
        res=res+n[i]
print(res)


#iteration

#size    res     i       x       n.append(x)     i%2==0    res+=n[i]  print(res)
#4        0      0       12         12            true      0+12=12       
#                1       23         23            false
#                2       43         43            false
#                3       56         56            true      12+56=68    68
