# 2  4  6  8  10
#12 14 16 18  20
#22 24 26 28  30
#32 34 36 38  40
#42 44 46 48  50

result=1
for i in range(5):
    for j in range(5):
        if(i<1):
            print(str(result*2)+" ",end=" ")
        else:
            print(result*2,end=" ")
        result+=1
    print()
