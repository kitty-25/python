#nested list
#cart=[]
#1.add item --> name, price, quantity, total -->if name is same,add quantity and calculate total
#2.remove item --> by getting name
#3.view details
#4.exit

cart={}
print("-------------")
print("Shopping Cart")
print("-------------")
option=int(input("1.Add Item\n2.Remove Item\n3.View Cart\n4.Exit\n"))
while option!=5:
    if(option==1):
        name=input("Enter the item:")
        quantity=int(input("Enter the item quantity:"))
        price=int(input("Enter the price of item:"))
        total=price*quantity
        cart[name]=[quantity, price, total]
        if name in cart.keys():
            print("This item is already added in the cart")
        print()
    elif(option == 2):
        name=input("Enter the item:")
        del(cart[name])
        print()
    elif(option==3):
        print("-----------------------------")
        print("Name  Quantity  Price   Total")
        print("-----------------------------")
        for name in cart:
            print(name, cart[name])
        print()
    elif(option==4):
        print("you exited the cart")
    else:
        pass
    print("-------------")
    print("Shopping Cart")
    print("-------------")
    option=int(input("1.Add Item\n2.Remove Item\n3.View Cart\n4.Exit\n"))
            
