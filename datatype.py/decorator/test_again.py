# Create a function multiply_all that accepts any number 
# of positional arguments and returns the product of all numbers.
# Display Profile Info
# Write a function display_profile that accepts 
# keyword arguments and prints each key and value on a new line.
# Log Function Call
# Create a decorator @logger that prints:
# The name of the function being called
# The arguments it was called with
# The result it returned
def multiply_all(*args):
    multiple=1
    for num in args:
        multiple=multiple*num
    return multiple

print(multiply_all(3,5,6))

def display_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
display_profile(name="Natasha", career="software engineering")
display_profile(name="Karani",status="married")
 
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def multiply_all(*args):
    multiple = 1
    for num in args:
        multiple *= num
    return multiple

# Example usage:
multiply_all(3, 4, 5, 6)
            