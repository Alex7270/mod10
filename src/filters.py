import re
from typing import Any


def filter_transactions(transactions: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """
    Фильтрация транзакций по заданному ключевому слову
    :param transactions: list[dict[str, Any]]
    :param search: str
    :return: list[dict[str, Any]]
    """
    new_lst = []
    for transaction in transactions:
        for i, value in transaction.items():
            if re.search(search, str(value), re.I):
                new_lst.append(transaction)
    return new_lst
