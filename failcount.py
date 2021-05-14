#Count on failed subjects

eng=int(input("Enter your english subject:"))
tam=int(input("Enter your tamil subject:"))
math=int(input("Enter your maths subject:"))

if ((eng>35) and (tam>35) and (math>35)):
    print("Passed all the subjects")
elif ((eng<35) and (tam<35) and (math<35)):
    print(f"Number of failed subjects is 3")
elif((eng<35) and (tam<35)):
    print(f"Number of failed subjects is 2")
elif((tam<35) and (math<35)):
    print(f"Number of failed subjects is 2")
elif((eng<35) and (math<35)):
    print(f"Number of failed subjects is 2")
else:
    print(f"Number of failed subjects is 1")
