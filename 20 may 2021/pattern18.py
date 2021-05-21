#0 1 0 1 0
#1 0 1 0 1
#0 1 0 1 0
#1 0 1 0 1
#0 1 0 1 0

for i in range(1,6):
    for j in range(1,6):
        res=i+j
        print(str(res%2),end=" ")
    print()
