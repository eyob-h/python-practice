import json
book = {}
book["mike"] = {
    'name' : 'Michael',
    'age' : 40,
    'role' : 'Point Guard'

}

book["russ"] = {
    'name' : 'Russell',
    'age' : 30,
    'role' : "Small Forward"
}
print(book)
print("-----")

jj = json.dumps(book, indent=4)
print(jj)

with open("jsonex.txt", "w") as file:
    file.write(jj)

z = dict()
with open("jsonex.txt", "r") as file:
    x = file.read()
    z = json.loads(x)


print("-----")
print("-----")
print(z["russ"]["age"])
print(type(z))

for dict(person) in z:
    print(type(person))