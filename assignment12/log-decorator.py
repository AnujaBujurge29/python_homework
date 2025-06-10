# one time setup
import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")

# Task 1: Set up logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))
...
# To write a log record:
logger.log(logging.INFO, "this string would be logged")


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log function name
        func_name = func.__name__
        # print(func_name)
        # Log positional parameters
        pos_params = "none" if not args else list(args)

        # Log keyword parameters
        kw_params = "none" if not kwargs else kwargs

        # Execute the function
        result = func(*args, **kwargs)

        # Log the information
        log_message = (
            f"function: {func_name} "
            f"positional parameters: {pos_params} "
            f"keyword parameters: {kw_params} "
            f"return: {result}"
        )
        logger.info(log_message)

        return result

    return wrapper

# 1.3 Function with no parameters


@logger_decorator
def say_hello():
    print("Hello, World!")
# 1.4 Function with variable positional arguments


@logger_decorator
def all_args(*args):
    return True

# 1.5 Function with variable keyword arguments


@logger_decorator
def keyword_args(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    # Test all functions
    say_hello()
    all_args(1, 2, 3, "test")
    keyword_args(name="John", age=30, city="New York")
