wordcount = dict()
with (open("wordcount.txt","r") )as file:
    for line in file:
        words = line.split(" ")
        words = line.split("\n")
        for word in words:
            if word not in wordcount:
                wordcount.update({word : 1})
            else:
                wordcount[word] += 1

        print(words)
    
    file.close()

print(wordcount)
