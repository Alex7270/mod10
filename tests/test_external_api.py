from typing import Any
from unittest.mock import patch

from src.external_api import get_convert_amount_rub, transaction_rub, transaction_usd


@patch("requests.request")
def test_get_convert_amount_rub(mock_get: Any) -> None:
    """
    Тестирование функции конвертации валюты из USD в RUB
    :param mock_get: Any
    :return: None
    """
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1747811534, "rate": 80.496455},
        "date": "2025-05-21",
        "result": 661791.140243,
    }
    assert get_convert_amount_rub(transaction_usd) == 661791.140243
    mock_get.assert_called_once()


def test_get_convert_amount_rub_rub() -> None:
    """
    Тестирование функции конвертации валюты из RUB в RUB
    :return: None
    """
    assert get_convert_amount_rub(transaction_rub) == 31957.58


def test_get_convert_amount_rub_incorrect(amount_incorrect: dict[str, Any]) -> None:
    """
    Тестирование функции конвертации валюты c некорректными данными
    :return: None
    """
    assert get_convert_amount_rub(amount_incorrect) == []


def test_get_convert_amount_rub_empty() -> None:
    """
    Тестирование функции конвертации валюты c отсутствующими данными
    :return: None
    """
    assert get_convert_amount_rub({}) == []
