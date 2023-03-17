import time
#using decorators
def time_it(function):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = function(*args, **kwargs)
        fin = time.time()

        print(f"{function.__name__} took {round((fin-st)*1000,2)} milliseconds")

        return result
    
    return wrapper

@time_it
def calc_square(num):
    # st = time.time()
    result=[]
    for i in range (num):
        sq = pow(i,2)
        result.append(sq)

    # fin = time.time()

    # print(f"Calc_square took {round((fin-st) *1000,2) } milliseconds")

    return result


@time_it
def calc_cube(num):
    # st = time.time()

    result=[]
    for i in range (num):
        cu = pow(i,3)
        result.append(cu)

    # fin = time.time()
    # print(f"Calc_square took {round((fin-st) *1000,2) } milliseconds")
    return result


(calc_square(5000))
(calc_cube(5000))


