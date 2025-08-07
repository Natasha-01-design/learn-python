import time

def time_func(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        fn(*args, **kwargs)
        end_time = time.time()
        diff = end_time - start_time
        print("Function took", diff, "seconds")
       
    return wrapper

@time_func
def calculate():
    l = 3 * 3
    W = 4 * 4
    sumed_up = l + W
    print("the sum is", sumed_up)
    
calculate()
    