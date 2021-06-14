#3 ints-a,b,c -->return their sum of their rounded values
#if your sum is 50 or more ->round up to multiple to 10
#if your sum is 50 or less ->round down to multiple to 10

def round_sum():
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    c=int(input("Enter a value:"))
    s=a+b+c
    #print(f"round_sum({a},{b},{c})-->")
    return s

def round10():
    num=round_sum()
    if num > 50:
        n=num//10
        print( n*10+10)
    else:
        n=num//10
        print( n*10)
     
round10()
round10()
round10()
