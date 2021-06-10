#display the longest word in the given string
n=input("Enter your string:")
l=n.split()
if len(l[0])>len(l[1]):
    print(l[0])
else:
    print(l[1])
