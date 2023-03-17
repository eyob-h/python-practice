# # def print_spam():
# #     print('spam')

# # def do_twice(ar):
# #     print(ar)
# #     print(ar)

# # do_twice(print_spam)

# def firstLine():
#     print("+ - - - - + - - - - +")

# def middleLine():
#     for i in range (4):
#         print("|         |         |")

# def twobytwo():
#     firstLine()
#     middleLine()
#     firstLine()

# twobytwo()
# twobytwo()

#recursion

numbers = 5

def factorials(num):
    print(num)
    sumOfAll = 0
    print("sum", sumOfAll)
    if num == 0:
        return (sumOfAll)
    else:
        sumOfAll += (num * (num-1))
        print("hh", sumOfAll) 
        factorials(num-1)
    
    return (sumOfAll)

print(factorials(5))