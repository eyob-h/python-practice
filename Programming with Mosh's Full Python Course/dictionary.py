#practice example 3
num_input = input("Enter numbers")

num = {'1':"ONE",
       '2':"TWO",
       '3':"THREE",
       '4': "FOUR",
       '5': "FIVE"}

op = ""
for i in num_input:
    op += num.get(i, "N") + " "

print(op)


#practice example 2

words = input(">")
coll = words.split(" ")
output = ""
map_it={"a":"z","b":"y","c":"x"}
for word in coll:
    for letter in word:
        output += map_it.get(letter) + " "

print (output)