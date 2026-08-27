from time import  time

current_time = time()
print(current_time)

def speeed_calc_decorator(function):
    def wrapper_function():
        start_time = time()
        function()
        end_time = time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speeed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speeed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i 

fast_function()
slow_function()
