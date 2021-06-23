#10 qns with 3 multiple choice options
#get ans from user and calculate marks
import random

user = input("Enter your name: ")
print(f"welcome to MCQ {user}")

q1 ="""Python is a ----------- language\na. interpreted\nb. object-oriented programming\nc. high-level\nd. low-level"""
q2 = """Is indentation required in Python?\na. Yes\nb. No\nc. Not sure\nd. Confused"""
q3 = """To start Python from the command prompt, use the command ______\na. execute python\nb. go python\nc. python\nd. run python"""
q4 = """What is the output of the following program :\ny = 8\nz = lambda x : x * y\nprint (z(6))\na. 48\nb. 14\nc. 64\nd. None of the above"""
q5 = """What is called when a function is defined inside a class?\na. Module\nb. Class\nc. Another Function\nd. Method"""
q6 = """Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?\na. [3, 4, 5, 20, 5, 25, 1, 3]\nb. [1, 3, 3, 4, 5, 5, 20, 25]\nc. [3, 5, 20, 5, 25, 1, 3]\nd. [1, 3, 4, 5, 20, 5, 25]"""
q7 = """Which of these is not a core data type?\na. Lists\nb. Dictionary\nc. Tuples\nd. Class"""
q8 = """Which of the following function convert a string to a float in python?\na. int(x [,base])\nb. long(x [,base] )\nc. float(x)\nd. str(x)"""
q9 = """What is the output of the following code :\nprint 9//2\na. 4.5\nb. 4.0\nc. 4\nd. Error"""
q10 = """Which function overloads the >> operator?\na. more()\nb. gt()\nc. ge()\nd. None of the above"""

qns = {q1:"a",q2:"c",q3:"c",q4:"a",q5:"d",q6:"c",q7:"d",q8:"c",q9:"c",q10:"d"}
mark=0
for i in qns:
    print(i)
    ans = input("Your ans: ")
    if ans == qns[i]:
        mark =  mark+1

print(f"{user} Your mark is {mark} out of 10")
