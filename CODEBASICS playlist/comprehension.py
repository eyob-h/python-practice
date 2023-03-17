#list comprehension
n = [1,2,3,4,5,6]
even = [i for i in n if i%2 == 0]
print(even)

square = [i*i for i in n]
print(square)

#set comprehension
s = set([1,2,3,4,5,5,3])
print(s)
ev = {i for i in s if i%2 ==0}
print(ev)

#dictionary comprhension
cities = ["adama","sheger","dire","robe"]
population_in_millions = [1.5,9,2,1.5]

pairs = {city:popln for city,popln in zip(cities,population_in_millions)}

for k in pairs:
    print(f"{k} = {str(pairs[k])} million")