#user to select the specialistion of the doctor

f = open("doctor.txt")

user = input("Enter the specialistion of the doctor: ")

for i in f:
    if user in i:
        print(i)


