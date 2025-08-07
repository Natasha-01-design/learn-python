import time
def time_update(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        diff=end_time-start_time
        print(f"function takes {diff} to run")
        log_msg = f"Function '{func.__name__}' took {diff} seconds to run\n"

        # Write the message to logger.txt
        with open("logger.txt", "a") as log_file:
            log_file.write(log_msg)
    return wrapper

@time_update
def calculate():
    l = 3 * 3
    W = 4 * 4
    sumed_up = l + W
    print("the sum is", sumed_up)

calculate()

def write_file(f_name,txt):
    with open(f_name,'w') as file:
        file.write(f"{txt}\n")

write_file(f_name="logger.txt",txt="Awesome")
