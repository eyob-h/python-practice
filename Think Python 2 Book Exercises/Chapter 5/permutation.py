a = 5


def permute(n):
    
    if n == 0 or n == 1:
        return 1
    
    else:
        return (n*permute(n-1))
    

print(permute(5))
