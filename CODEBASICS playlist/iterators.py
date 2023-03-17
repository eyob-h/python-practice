#socratica iterators tut

# for loop behind the scenes
names = ['mrx','mry','mrz']

looper = iter(names)

while True:
    try:
        names = next(looper)
        print (names)
    except StopIteration:
        break


print("=======")
class Remote:
    def __init__ (self):
        self.channels = ['etv','ebs','nahoo']
        self.index = -1

    def __iter__ (self):
        return self
    
    def __next__(self):
        self.index += 1

        if (self.index == len(self.channels)):
            raise StopIteration
        
        
        return self.channels[self.index]
    
r = Remote()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
# print(r.__next__)


print("++++++++++++++++++++++")

#simple iterator
lis = ["mra", "mrb","mrc"]
itr = reversed(lis)
print(next(itr))
print(next(itr))
print(next(itr))