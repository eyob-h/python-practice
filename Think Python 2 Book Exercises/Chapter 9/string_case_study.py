# import os
# curr = os.getcwd()

fin = open("c:/Users/Eyob 2/Desktop/PYTHON/Think Python 2 Book Exercises/Chapter 9/words.txt")
# print(curr)

word = fin.readline()
word.strip()
print(word)

# for line in (fin):
#     word = line.strip()
#     if(len(word)>20):
#         print (word)  

print("+++++++++++++++++")
      
# for lines in (fin):
#     words = lines.strip()
#     if(word.count("e")== 0):
#         print (words) 
    
# s = "hithere friend"     

for wrd in fin:
    if wrd.count("e") == 4:
        print(wrd, end=" ")
        print(wrd.count("e"))   

# s = fin.readline()
fin = open("c:/Users/Eyob 2/Desktop/PYTHON/Think Python 2 Book Exercises/Chapter 9/words.txt")

for letters in fin:
    for words in letters:
        if "e" not in words:
            print("No E")