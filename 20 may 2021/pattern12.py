#1  6 11 16 21
#2  7 12 17 22
#3  8 13 18 23
#4  9 14 19 24
#5 10 15 20 25

res=5
for i in range(1,6):
    
    for j in range(1,6):
        if i<5:
            print(str(i),end="  ")
        else:
            print(str(i),end=" ")
        i+=res
    print()
        
            
            
        
    
        
