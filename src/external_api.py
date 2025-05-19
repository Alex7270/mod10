import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import get_transaction

transactions_lst = get_transaction("data/operations.json")


def get_convert_amount_rub(transaction: dict[str, Any]) -> Any | None:
    """
    Функция возвращает сумму транзакции в рублях, если транзакция была в USD или EUR конвертирует в рубли.
    :param transaction: dict[str, Any]
    :return: list[float]
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    # Загрузка переменных из .env-файла
    load_dotenv()

    # Получение значения переменной API_KEY из .env-файла
    api_key = os.getenv("API_KEY")

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {"amount": amount, "from": currency, "to": "RUB"}

        headers = {"apikey": api_key}

        response = requests.request("GET", url, headers=headers, params=payload)

        status_code = response.status_code
        result = response.text

        if status_code == 200:
            return json.loads(result).get("result")
        return "Ошибка передачи данных"
    return None
