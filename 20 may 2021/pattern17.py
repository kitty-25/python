#1  3  5  7  9
#3  5  7  9 11
#5  7  9 11 13
#7  9 11 13 15
#9 11 13 15 17


for i in range(10):
    for j in range(10):
        if(i%2==1 and j%2==1):
            print(str(i+j-1),end=" ")
    print()
