import random

n=['Head', 'Tail']
user=input("Choose Head or Tail: ")
print(f"Toss is: {random.choice(n)}")
if user == random.choice(n):
    print("You won")
else:
    print("You lose")

