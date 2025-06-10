from functools import wraps
# 2.2 Declare a decorator


def type_converter(type_of_output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# 2.3


@type_converter(str)
def return_int():
    return 5
# 2.4


@type_converter(int)
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)  # This should print "str"
try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    # This is what should happen
    print("can't convert that string to an integer!")
