from typing import Any

from src.countings import counting_categories


def test_counting_categories(
    transactions: list[dict[str, Any]], categories_operations: list[str], expected_counting_categories: dict[str, int]
) -> None:
    """
    Функция тестирования количества операций в каждой категории
    :param:  transactions: list[dict[str, Any]]
    :param:  categories_operations: list[str]
    :param:  expected_counting_categories: dict[str, int]
    :return: None
    """
    assert counting_categories(transactions, categories_operations) == expected_counting_categories


def test_counting_categories_empty(transactions: list[dict[str, Any]], categories_operations: list[str]) -> None:
    """
    Функция тестирования количества операций в каждой категории, категории не заданы
    :param:  transactions: list[dict[str, Any]]
    :param:  categories_operations: list[str]
    :return: None
    """
    assert counting_categories(transactions, []) == {}


def test_counting_categories_incorrect(categories_operations: list[str]) -> None:
    """
    Функция тестирования количества операций в каждой категории
    :param:  transactions: list[dict[str, Any]]
    :param:  categories_operations: list[str]
    :return: None
    """
    assert counting_categories([], categories_operations) == {}
