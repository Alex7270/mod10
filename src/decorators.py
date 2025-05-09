from datetime import datetime


def log(filename="mylog.txt"):
    def my_decorator(function):
        def wrapper(*args, **kwargs):
            print(datetime.now())
            result = function(*args, **kwargs)
            print(datetime.now())
            return result

        return wrapper

    return my_decorator
