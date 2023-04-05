# Car racing word simulation

# exit_program = False
# while exit_program != True:
#     car_state = input()
#     match car_state:
#         case "help":
#             print("start = to start the car")
#             print("stop = to stop the car")
#             print("quit = to exit")
#         case "start":
#             print("Car started...Ready to Go!")
#         case "stop":
#             print("Car stopped!")
#         case "quit":
#             exit_program = True
#         case _:
#             print("I don't know that command")

# Delete the duplicates in the lists

numbers = [3,5,6,7,4,3,23,5,5,5,66,4,32,4,4,4,32,5,6,8]
numbers.sort()
print(f"With duplicates: {numbers}")

no_dup = []
for i in numbers:
    if i not in no_dup:
        no_dup.append(i)

print(f"Duplicates removed: {no_dup}")


# List and tuple unpacking
ll = [1,2,3,4]
a, b, c, d = ll 

tpl = (11,23,33)
x,y,z, h = tpl

print(a, y , z )
