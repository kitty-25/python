#find sum of digits in the given number(eg:153 --> 1+5+3=9; 67-->6+7=13)

n=int(input())
sum=0
while n!=0:
    sum+=n%10
    n//=10   #n=n//10
print(sum)
