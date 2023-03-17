print("Mission Control")
def mc(n):
    if n == 0:
        print("Blast OFF")
        return
    else:
        print("T-Minus", n, "seconds")
        mc(n-1)

mc(5)