x = 5 
y = "a"

try:
    z = x/y
    print (z)
except Exception as e:
    print("Exception type: ", type(e).__name__)

