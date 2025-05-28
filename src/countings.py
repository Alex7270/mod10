from collections import Counter
from typing import Any


def counting_categories(transactions: list[dict[str, Any]], categories_operations: list[str]) -> dict[str, int]:
    """
    Считает количество операций в каждой категории
    :params transactions: list[dict[str, Any]]
    :params categories_operations: list[str])
    :return: dict[str: int]
    """
    descriptions = []
    for transaction in transactions:
        if (
            str(transaction.get("description")) != "nan"
            and str(transaction.get("description")) in categories_operations
        ):
            descriptions.append(str(transaction.get("description")))
    return dict(Counter(descriptions))
