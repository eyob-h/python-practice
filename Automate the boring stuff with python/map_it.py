import argparse
import webbrowser
import sys
import pyperclip

if (len(sys.argv)>0):
    address = ''.join(sys.argv[1:])
else:
    # address = input("Please enter the address")
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)




# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("x_coor", help="x-coordinate")
#     parser.add_argument("y_coor", help="y-coordinate")
#     # parser.add_argument("num1", help="first number")
#     # parser.add_argument("num2", help="second number")

#     arg = parser.parse_args()

#     print(arg.x_coor)
#     print(arg.y_coor)

# arg.x_coor = int(arg.x_coor)
# arg.y_coor = int(arg.y_coor)