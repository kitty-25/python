#program to register doctor's info

name = input("Doctor Name: ")
mobile = input("Mobile no: ")
specialisation = input("Specialisation: ")
timing = input("Timing: ")
cost = input("Cost: ")

f = open("doctor.txt")
data = f.readlines()
f.close()

if mobile not in str(data):
    f = open("doctor.txt","a")
    f.write(name+" "+mobile+" "+specialisation+" "+timing+" "+cost+"\n")
    print("Registration is done successfully")
    f.close()
else:
    print("Mobile number already exists")
