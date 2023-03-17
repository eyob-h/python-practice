# #sundeep's tut
# argv, argc

# import sys

# print(sys.argv)
# print("======")

# #displaying elements using command line argument

# for i in range (len(sys.argv)):
#     print(sys.argv[i])


# #adding elements using command line argument

# sum = 0
# for i in range (1, len(sys.argv)): #start from 1 as the first element of argv is the file name
#     sum += int(sys.argv[i])
# print(f"sum of elements = {sum}")

#codebasic's tut
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num1", help="first number")
    parser.add_argument("num2", help="second number")
    parser.add_argument("--op", help="operation b\\n the 2")

    arg = parser.parse_args()

    print(arg.num1)
    print(arg.num2)
    print(arg.op)

arg.num1 = int(arg.num1)
arg.num2 = int(arg.num2)

if arg.op == "add":
    print(arg.num1+arg.num2)

elif arg.op == "sub":
    print(arg.num1-arg.num2)

elif arg.op == "mul":
    print(arg.num1*arg.num2)

elif arg.op == "div":
    print(arg.num1/arg.num2)

elif arg.op == "sqr":
    print(pow(arg.num1,2), arg.num2**2)

