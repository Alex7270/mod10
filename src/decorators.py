from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Any], Callable[[int, int], Any]]:
    def my_decorator(func: Any) -> Callable[[int, int], Any]:
        @wraps(func)
        def wrapper(*args: int, **kwargs: int) -> Any:
            try:
                datetime.now()
                result = func(*args, **kwargs)
                datetime.now()
                message = (
                    f"Начало работы функции: {datetime.now()}\n\n"
                    f"Имя функции: {func.__name__}\n{func.__doc__}\n"
                    f"Аргументы функции args: {args}; kwargs: {kwargs}\n\n"
                    f"Окончание работы функции: {datetime.now()}\n\nРезультат работы функции: OK\n"
                )
                if filename:

                    with open("data/" + filename, "a", encoding="utf-8") as file:
                        file.write(message)
                else:
                    print(message)

                return result

            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open("data/" + filename, "a") as file:
                        file.write(message)
                else:
                    print(message)
            raise

        return wrapper

    return my_decorator
