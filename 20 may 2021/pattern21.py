#0 1 0 1 0
#0 0 0 0 0
#0 1 0 1 0
#0 0 0 0 0
#0 1 0 1 0

for i in range(1,6):
    for j in range(1,6):
        res=i+j
        if i%2==1:
            print(str(res%2),end=" ")
        else:
            print("0",end=" ")
    print()
