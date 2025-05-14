import os
from typing import Any

from src.decorators import log


def test_log(capsys: Any, expected_str: str) -> None:
    """
    Функция тестирования декоратора log при отсутствии параметров и вывода результатов в консоль
    :param capsys: Any
    :param expected_str: str
    :return: None
    """

    @log()
    def add_numbers(a: float, b: float) -> float:
        return a + b

    add_numbers(2, 3)
    captured = capsys.readouterr()
    assert expected_str in captured.out


def test_log_param(expected_str: str) -> None:
    """
    Функция тестирования декоратора log при наличии параметров и записи результатов в файл
    :param expected_str: str
    :return: None
    """

    @log(filename="mylog2.txt")
    def add_numbers(a: float, b: float) -> float:
        return a + b

    try:
        add_numbers(2, 3)

        # Проверяем содержимое файла mylog2.txt
        with open("data/mylog2.txt", "r", encoding="utf-8") as file:
            logs = file.read()
            assert expected_str in logs

    finally:
        # Удаляем временный файл
        os.remove("data/mylog2.txt")


def test_log_error(capsys: Any, expected_error: str) -> None:
    """
    Функция тестирования декоратора log при отсутствии параметров и вывода ошибки в консоль
    :param capsys: Any
    :param expected_error: str
    :return: None
    """

    @log()
    def add_numbers(a: float, b: float) -> float:
        return a + b

    add_numbers(2)
    captured = capsys.readouterr()
    assert expected_error in captured.out


def test_log_param_error(expected_error: str) -> None:
    """
    Функция тестирования декоратора log при наличии параметров и записи ошибки в файл
    :param expected_error: str
    :return: None
    """

    @log(filename="mylog2.txt")
    def add_numbers(a: float, b: float) -> float:
        return a + b

    try:
        add_numbers(2)

        # Проверяем содержимое файла mylog2.txt
        with open("data/mylog2.txt", "r", encoding="utf-8") as file:
            logs = file.read()
            assert expected_error in logs

    finally:
        # Удаляем временный файл
        os.remove("data/mylog2.txt")
