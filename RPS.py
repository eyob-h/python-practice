import random

#r>s>p

def play():
    # computer = random.choice(['r','p','s'])
    # # print(f"Computer: {computer}")
    # print("==============")

    # user = input("ROCK, PAPER, OR, SCISSORS?")
    # user = user.lower()
    # res = RPScheck(user,computer)

    # print(res)
    res = ""
    while res != "you won":
        computer = random.choice(['r','p','s'])
        user = input("ROCK, PAPER, OR, SCISSORS?")
        user = user.lower()
        res = RPScheck(user,computer)
        print("==============")
        print(f"Computer {computer}")
        print(res)

        print("==============")


def RPScheck(user,computer):

    if(user==computer):
        return "tied"
    
    elif((user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r')):
        return "you won"
    
    return "you lost"


play()
