from datetime import datetime
from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    """
    Функция тестирования декоратора log при отсутствии параметров и вывода результатов в консоль
    """

    @log()
    def add_numbers(a: float, b: float) -> float:
        return a + b

    add_numbers(2, 3)
    captured = capsys.readouterr()
    assert (
        captured.out == f"\nНачало работы функции: {datetime.now()}\n\nИмя функции: add_numbers\nNone\n"
        f"Аргументы функции args: (2, 3); kwargs: {{}}\n\nОкончание работы функции: {datetime.now()}\n\n"
        f"Результат работы функции ОК: \n 5\n\n"
    )
