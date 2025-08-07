def greet (*args):
    for arg in args:
        print(f"Hello, {arg}!")
greet ("Natasha")

def my_sum(r, *args):
    area = 3.142 * r * r
    print("Sum is", sum(args))
    print("area is", area)

my_sum(5, 3, 4, 5)  # Here, r=5, and the rest are summed
    