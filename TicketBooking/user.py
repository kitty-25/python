import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017")
db = con["booking"]
col = db["user"]


totalseats = 120

name = input("Enter your name:")
mobile = int(input("Enter your mobile number:"))
soldseats = int(input("Enter how many seats you want to book:"))
category = input("Enter which category of seats you want(A/B/C):")
if category == 'A':
    price = 40
    totalamount = price* soldseats
elif category == 'B':
    price = 30
    totalamount = price * soldseats
else:
    price = 20
    totalamount = price * soldseats

def display():
    print("----------------------")
    print("-----Your Ticket------")
    print("----------------------")
    print(f"Name : {name}")
    print(f"Mobile : {mobile}")
    print(f"Number of Seats : {soldseats}")
    print(f"Seat Category : {category}")
    print(f"Total Amount : {totalamount}")
    print("----------------------")
    print("------Thank You!------")
    print("----------------------")

option = input("would you like to confirm your tickets (Yes/No):")
if option == "Yes":
    vacantseats = totalseats - soldseats
    col.insert_one({"Name": name, "Mobile": mobile,"Total Seats":totalseats, "Number of Seats": soldseats, "Seat Category": category,"Total Amount": totalamount, "Vacant Seats": vacantseats})
    col.update_one({"Vacanct Seats":vacantseats},{"$set":{"Total Seats":totalseats}})
    display()
else:
    print("Your ticket has been cancelled. Thank You!")
