from datetime import datetime
from functools import wraps
from typing import Any, Generator


def log(filename: str = "mylog.txt"):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Начало работы функции {datetime.now()}")
            print(f"Имя функции {func.__name__}")
            print(f"Аргументы декоратора: {filename}")
            print(func.__doc__)
            result = func(*args, **kwargs)
            print(f"Окончание работы функции {datetime.now()}")
            print("Результат работы функции:")
            return result

        return wrapper

    return my_decorator
