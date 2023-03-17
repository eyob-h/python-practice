# # def fib(n):
# #     if n == 1:
# #         return 1
    
# #     elif n == 0:
# #         return 0
    
# #     if(n>1):
# #         return fib(n-1) + fib(n-2)
    
    

# # print(fib(6))


# wrd = "hithere"
# print(wrd)
# a = wrd.replace("h","a")
# print(wrd)
# print(a)


def is_reverse(word1, word2):
    if len(word1) != len(word2):
     return False
    i = 0
    j = len(word2)-1
    while j > -1:
        print(i,j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

print(is_reverse("hi", "ah"))
print(is_reverse("pots", "stop"))

