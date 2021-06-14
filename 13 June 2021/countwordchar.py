#count of words and characters

sentence=input("Enter a sentence:")
count=sentence.split(" ")
wordcount=len(count)
print(f"Your sentence has {wordcount} word(s)")
print("Each word has the following number of characters:")
for char in count:
    charcount = len(char)
    print(charcount, end=" ")
print("character(s)")
