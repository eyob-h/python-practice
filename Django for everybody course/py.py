# # Enter your code here. Read input from STDIN. Print output to STDOUT
# if __name__ == '__main__':
#     n = int(input())
#     m = int(input())

# dash = ((m-7)/2)    
for i in range (5):
    # for j in range(i+1):
    #     print("-",end="")
    
   

    for j in range(5-i):
        print(" ",end="")

    for j in range(i):
        print(".|.",end="")
    for j in range(i+1):
        print(".|.",end="")

    # for j in range(5-i):
    #    print("-",end="")

    print()
    
