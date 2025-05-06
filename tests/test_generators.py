from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
    ],
)
def test_filter_by_currency_correct(
    transactions: list[dict[str, Any]], currency: str, expected: list[dict[str, Any]]
) -> None:
    """
    Функция тестирования фильтрации транзакций по заданной валюте 'USD'
    :param transactions: list[dict[str, Any]]
    :param currency: str
    :return: None
    """
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.mark.parametrize(
    "currency, expected",
    [
        ("USD", []),
        ("EUR", []),
        ("USD", []),
        ("USD", []),
    ],
)
def test_filter_by_currency_incorrect(
    transactions_incorrect: list[dict[str, Any]], currency: str, expected: list[dict[str, Any]]
) -> None:
    """
    Функция тестирования фильтрации транзакций c некорректными данными
    :param transactions_incorrect: list[dict[str, Any]]
    :param currency: str
    :param expected: dict[str, Any]
    :return: None
    """
    result = list(filter_by_currency(transactions_incorrect, currency))
    assert result == expected


def test_filter_by_currency_empty() -> None:
    result = list(filter_by_currency([], ""))
    assert result == []


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "Перевод организации",
        ),
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "Перевод со счета на счет",
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
            "Перевод со счета на счет",
        ),
        (
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
            "Перевод с карты на карту",
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "Перевод организации",
        ),
    ],
)
def test_transaction_descriptions(transactions: list[dict[str, Any]], expected: list[dict[str, Any]]) -> None:
    """
    Функция тестирования транзакций c описанием каждой операции по очереди
    :param transactions: list[dict[str, Any]]
    :param expected: list[dict[str, Any]]
    :return: None
    """
    descriptions = transaction_descriptions(transactions)
    for i in descriptions:
        assert i == expected


@pytest.mark.parametrize(
    "description_incorrect, expected",
    [
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "escription": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "No data",
        ),
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "",
        ),
        ([], []),
    ],
)
def test_transaction_descriptions_incorrect(description_incorrect: list[dict[str, Any]], expected: str) -> None:
    """
    Функция тестирования транзакций c некорректными данными description
    :param description_incorrect: list[dict[str, Any]]
    :param expected: str
    :return: None
    """
    descriptions = transaction_descriptions(description_incorrect)
    for i in descriptions:
        assert i == expected


@pytest.mark.parametrize(
    "start, stop, expected_number",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999995,
            10**16,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, stop: int, expected_number: list[str]) -> None:
    """
    Функция тестирования генератора номеров банковских карт в формате XXXX XXXX XXXX XXXX
    """
    card_number = list(card_number_generator(start, stop))
    assert card_number == expected_number
