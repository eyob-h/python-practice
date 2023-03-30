exit_program = False
while exit_program != True:
    car_state = input()
    match car_state:
        case "help":
            print("start = to start the car")
            print("stop = to stop the car")
            print("quit = to exit")
        case "start":
            print("Car started...Ready to Go!")
        case "stop":
            print("Car stopped!")
        case "quit":
            exit_program = True
        case _:
            print("I don't know that command")