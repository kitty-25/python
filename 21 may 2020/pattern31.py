#A B C D E 
#B C D E F 
#C D E F G 
#D E F G H 
#E F G H I 

for i in range(65,70):
    res=i
    for j in range(5):
        print(chr(res),end=" ")
        res+=1
    print()
