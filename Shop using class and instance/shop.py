class Product:
    brand = 'apple'

    def getinfo(obj):
        obj.item = input("Enter the product: ")
        obj.itemcolor = input("Enter the colour of the product you need: ")
        obj.price = int(input("Enter the price of the product: "))

    def display(obj):
        print("--------------------------------------")
        print("--------Your Product Details----------")
        print("--------------------------------------")
        print(f"your product brand is: {Product.brand}")
        print(f"your product is: {obj.item}")
        print(f"your product colour is: {obj.itemcolor}")
        print(f"your product price is: {obj.price}")
        print("--------------------------------------")
        print("-------------Thank You!---------------")
        print("--------------------------------------")

Macbook = Product()
Macbook.getinfo()
Macbook.display()

Iphone = Product()
Iphone.getinfo()
Iphone.display()

Ipad = Product()
Ipad.getinfo()
Ipad.display()


