# def count_substring(string, sub_string):
#     counter = 0
#     for i in range(0,len(string):
#         if(sub_string == i):
#             counter +=1
#     return counter

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


n = int(input())
arr = map(int, input().split())

listn = []    
for i in arr:
    listn.append(i)


def runner_up(list_input):
    list_input.sort(reverse=True)
    highest = max(list_input)
    for i in list_input:
        if(i < highest):
            return i

print(runner_up(list_n)        