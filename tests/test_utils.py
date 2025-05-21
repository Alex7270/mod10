from typing import Any
from unittest.mock import patch

from src.utils import get_transaction


@patch("json.load")
def test_get_transaction_correct(mock_loads: Any, path: str, expected_correct: list[dict[str, Any]]) -> None:
    """
    Тестирование функции с корректными данными о финансовых транзакциях
    :param mock_loads: Any
    :param path: str
    :param expected_correct: list[dict[str, Any]]
    :return: None
    """
    mock_loads.return_value = expected_correct
    assert get_transaction(path) == expected_correct
    mock_loads.assert_called_once()


@patch("json.load")
def test_get_transaction_incorrect(mock_loads: Any, path_incorrect: str) -> None:
    """
    Тестирование функции с не корректными данными пути к файлу
    :param mock_loads: Any
    :param path_incorrect: str
    :return: None
    """
    mock_loads.return_value = []
    assert get_transaction(path_incorrect) == []


@patch("json.load")
def test_get_transaction_empty(mock_loads: Any, path_file_empty: str) -> None:
    """
    Тестирование функции с некорректными данными о финансовых транзакциях
    :param mock_loads: Any
    :param path_file_empty: str
    :return: None
    """
    mock_loads.return_value = []
    assert get_transaction(path_file_empty) == []
    mock_loads.assert_called_once()
