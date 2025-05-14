from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Any], Callable[[int, int], Any]]:
    """
    Декоратор ведет лог работы функции и ее результат, а также возникшие ошибки как в файл, так и в консоль.
    :param filename: str | None
    :return: Callable[[Any], Callable[[int, int], Any]]
    """

    def my_decorator(func: Any) -> Callable[[int, int], Any]:
        @wraps(func)
        def wrapper(*args: int, **kwargs: int) -> Any:
            try:
                datetime.now().strftime("%Y-%m-%d %X")
                result = func(*args, **kwargs)
                datetime.now().strftime("%Y-%m-%d %X")
                message = f"\n{datetime.now().strftime('%Y-%m-%d %X')} {func.__name__} ОК: {result}"
                if filename:

                    with open("data/" + filename, "a", encoding="utf-8") as file:
                        file.write(message)

                else:
                    print(message)

                return result

            except (TypeError, ValueError) as e:
                message = (
                    f"\n{datetime.now().strftime('%Y-%m-%d %X')}"
                    f" {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                )
                if filename:
                    with open("data/" + filename, "a", encoding="utf-8") as file:
                        file.write(message)
                else:
                    print(message)

        return wrapper

    return my_decorator
