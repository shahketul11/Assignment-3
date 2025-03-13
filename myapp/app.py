from myapp.mymodule.funcs import multiply, divide


def multiply_by_two(x):
    return multiply(x, 2)


def divide_by_two(x):
    return divide(x, 2)

def calculate_area(side_length):

    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number")
    
    return side_length ** 2


