import string
fin = open("book.txt", "r")
x = fin.read()
print(x)

strs = string.punctuation
print(strs)

for i in fin:
    if i in strs:
        print("punction")
    else:
        print("no")