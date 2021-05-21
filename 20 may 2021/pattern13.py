#1 10 11 20 21
#2  9 12 17 22
#3  8 13 18 23
#4  7 14 17 24
#5  6 15 16 25

res=5
for i in range(1,6):
    a=res-i+1
    for j in range(1,6):
        if j%2==1 and i>1:
            print(str(i),end="  ")
        else:
            print(str(a),end=" ")
        i+=res
        a+=res
    print()
