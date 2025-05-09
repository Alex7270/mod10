from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str = "mylog.txt") -> Callable[[Any], Callable[[int, int], Any]]:
    def my_decorator(func: Any) -> Callable[[int, int], Any]:
        @wraps(func)
        def wrapper(*args: int, **kwargs: int) -> Any:
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
