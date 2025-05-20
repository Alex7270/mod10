from typing import Any

from src.utils import get_transaction


def test_get_transaction_correct(path: str, expected_correct: list[dict[str, Any]]) -> None:
    """
    Тестирование функции с корректными данными о финансовых транзакциях
    :param path: str
    :return: None
    """

    assert get_transaction(path) == expected_correct
