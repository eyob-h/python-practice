class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def print_out_message(self):
        print(f"User defined exception: {self.msg} ")


try:
    raise Accident("Crash of the carsa")
except Accident as e:
    e.print_out_message()
finally:
    print("Executed even if exception occurs")
    # f.close()
