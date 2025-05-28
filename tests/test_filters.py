from typing import Any

from src.filters import filter_transactions


def test_filter_transactions(transactions: list[dict[str, Any]], expected_filter: list[dict[str, Any]]) -> None:
    """
    Тестирование функции фильтрации транзакций по заданному ключевому слову
    :param transactions: list[dict[str, Any]]
    :param expected_filter: list[dict[str, Any]]
    :return: None
    """
    assert filter_transactions(transactions, "перевод") == expected_filter


def test_filter_transactions_no_search(
    transactions: list[dict[str, Any]], expected_filter: list[dict[str, Any]]
) -> None:
    """
    Тестирование функции фильтрации транзакций при отсутствии ключевого слова в транзакции
    :param transactions: list[dict[str, Any]]
    :param: expected_filter: list[dict[str, Any]]
    :return: None
    """
    assert filter_transactions(transactions, "kkkkkk") == []
