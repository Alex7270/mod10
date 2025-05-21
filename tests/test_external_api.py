from typing import Any
from unittest.mock import patch

from src.external_api import get_convert_amount_rub, transaction_usd


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
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "NCc6mcT98gWEvtVGunXHoICvZuhYT9l6"},
        params={"amount": "8221.37", "from": "USD", "to": "RUB"},
        timeout=50,
    )
