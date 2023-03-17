import datetime

usr_input = input("Enter your goal with the deadline separated by ':'")
inpt = usr_input.split(":")

goal = inpt[0]
deadline = inpt[1]

print (goal)
print (deadline)
print (inpt)

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)
today = datetime.datetime.today()
time_left = today - deadline_date

print( f"You have: {time_left.days} days left for {goal}")