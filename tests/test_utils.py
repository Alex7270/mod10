from typing import Any

from src.utils import get_transaction


def test_get_transaction_correct(path: str, expected_correct: list[dict[str, Any]]) -> None:
    """
    Тестирование функции с корректными данными о финансовых транзакциях
    :param path: str
    :return: None
    """

    assert get_transaction(path) == expected_correct


def test_get_transaction_incorrect() -> None:
    """
    Тестирование функции с не корректными данными пути к файлу
    :return:
    """

    assert get_transaction("") == []


def test_get_transaction_empty() -> None:
    """
    Тестирование функции с не корректными данными о финансовых транзакциях
    :return:
    """

    assert get_transaction("data/operation_empty.json") == []
