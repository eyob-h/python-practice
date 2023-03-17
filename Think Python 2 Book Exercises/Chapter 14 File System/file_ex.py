import os
import dbm

# if  os.path.exists("output.txt"):
#     print("cool")
# else:
#     fout = open("output.txt", "w")

#     line1 = "This is PYTHON \n"
#     line2 = "The coolest language in the world \n"

#     fout.write(line1)
#     fout.write(line2)
#     fout.close()

cats = 88
# cats = "%d" %cats
print (type(cats))


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# walk(os.getcwd())

try:
    os.listdir(cats.txt)
except:
    print("Try Again")


database = dbm.open("caption", 'c')
