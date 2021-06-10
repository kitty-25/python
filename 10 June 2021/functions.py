#square, cube, factorial, sumofseries(1+2+...+n)

n=int(input("Enter a number:"))

def square():
    a=n*n
    print(f"Square is: {a}")

def cube():
    b=n*n*n
    print(f"Cube is: {b}")

def factorial():
    fact=1
    for i in range(1,n):
        fact*=i
    print(f"Factorial is: {fact*n}")

def sumofseries():
    sum=0
    for i in range(n):
        sum+=i
    print(f"Sum of series is: {sum}")

square()
cube()
factorial()
sumofseries()
