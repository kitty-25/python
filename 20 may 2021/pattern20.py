#1 0 1 0 1
#0 0 0 0 0
#1 0 1 0 1
#0 0 0 0 0
#1 0 1 0 1

for i in range(2,7):
    for j in range(1,6):
        res=i+j
        if i%2==0:
            print(str(res%2),end=" ")
        else:
            print("0",end=" ")
    print()
