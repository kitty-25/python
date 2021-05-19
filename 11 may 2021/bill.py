#calculate the total amount for 5 products
name1=input("Item1:")
price1=float(input("Price:"))
qty1=int(input("Qty:"))
total1=qty1*price1
print(total1)

name2=input("Item2:")
price2=float(input("Price:"))
qty2=int(input("Qty:"))
total2=qty2*price2
print(total2)

name3=input("Item3:")
price3=float(input("Price:"))
qty3=int(input("Qty:"))
total3=qty3*price3
print(total3)

name4=input("Item4:")
price4=float(input("Price:"))
qty4=int(input("Qty:"))
total4=qty4*price4
print(total4)

name5=input("Item5:")
price5=float(input("Price:"))
qty5=int(input("Qty:"))
total5=qty5*price5
print(total5)

net=total1+total2+total3+total4+total5

print(f"Items Price Qty Total")
print(f"{name1}    {price1}    {qty1}  {total1}")
print(f"{name2}    {price2}    {qty2}  {total2}")
print(f"{name3}    {price3}    {qty3}  {total3}")
print(f"{name4}    {price4}    {qty4}  {total4}")
print(f"{name5}    {price5}    {qty5}  {total5}")
print(f"Net Amount: {net}")

