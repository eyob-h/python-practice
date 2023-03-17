
users = ['russ','mike','steph','kd','cp','melo']

def gen():
    
    for i in users:
        yield i   #yield is what makes it an generator


itr = gen()

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


print("++++++++++++++++")
#fibonacci sequence with generators

def fib():
    a, b = 0 , 1
    while True:
        yield a
        a , b = b, a+b

for f in fib():
    if f> 10000000000:
        break
    print (f)


def fib2():
    a, b = 0, 1

    while True:
        yield a
        a, b = b , a+b


for i in fib():
    if i > 50:
        break
    print(i)

fib2()