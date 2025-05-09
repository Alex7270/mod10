from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log() -> Callable[[Any], Callable[[int, int], Any]]:
    def my_decorator(func: Any) -> Callable[[int, int], Any]:
        @wraps(func)
        def wrapper(*args: int, **kwargs: int) -> Any:
            result = func(*args, **kwargs)
            print(
                f"Начало работы функции: {datetime.now()}\n\nИмя функции: {func.__name__}\n{func.__doc__}\n"
                f"Аргументы функции args: {args}; kwargs: {kwargs}\n\nОкончание работы функции: {datetime.now()}\n\n"
                f"Результат работы функции:\n"
            )
            return result

        return wrapper

    return my_decorator
