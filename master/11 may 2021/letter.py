#Auto-generating permission/leave letter

whom=input("To whom you are writing:")
reason=input("Reason for getting permission/leave:")
leave=input("How many days/hours you need leave/permission:")
name=input("Your name:")
date=input("Date:")

print(f"-----------------------------")
print(f"Dear {whom},")
print(f"Greetings of the day.")
print(f"As I am suffering from {reason}. I am not able to attend your session. so, I kindly request you to grant me leave/permission for {leave} days/hrs. ")
print(f"Thanking you.")
print(f"Kind Regards,")
print(name)
print(date)
