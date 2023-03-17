# dr = {}
# dr["one"] = "and"
# dr["two"] = "hulet"

# print(dr["one"])
# print("two" in dr)


# str = "abcabcabcabcabcabcabcabcabcagjhkjhkhkbc"

# dt = {}
# for letter in str:
#     if letter in dt:
#         dt[letter] += 1
#     else:
#         dt[letter] = 1

# print(dt)


#memoization
memTable = {0:0, 1:1}

def fib(n):
    if(n in memTable):
        return memTable[n]
    
    result = fib(n-1) + fib(n-2)
    memTable[n] = result
    return result

print(fib(10))

t=(7,3)
x= divmod(*t)
print(x)


