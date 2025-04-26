import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "correct_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_correct(correct_number: str, expected: str) -> None:
    """
    Функция тестирования корректного распознавания и маскировки
    в зависимости от типа входных данных (карта или счет)
    :param correct_number: str    :return: str
    """
    assert mask_account_card(correct_number) == expected


@pytest.mark.parametrize(
    "incorrect_number, expected",
    [
        ("", "Вы не ввели номер"),
        ("Счет", "Вы не ввели номер"),
        ("MasterCard", "Вы не ввели номер"),
        ("Счет  35383__033474447895560", "Счет Введен некорректный номер счета"),
        ("Visa  Classic 68319824767 37658", "Visa Classic Введен некорректный номер карты"),
        ("Visa Platinum 89  90922113665229", "Visa Platinum Введен некорректный номер карты"),
        ("Visa Gold 59994---14228426353", "Visa Gold Введен некорректный номер карты"),
        (" Счет 7365410  hhh8430135874305  ", "Счет Введен некорректный номер счета"),
    ],
)
def test_mask_account_card_incorrect(incorrect_number: str, expected: str) -> None:
    """
    Функция тестирования некорректных входных данных и проверка ее устойчивости к ошибкам
    :param incorrect_number: str    :return: str
    """
    assert mask_account_card(incorrect_number) == expected


@pytest.mark.parametrize(
    "correct_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-12T02:26:19.671407", "12.05.2024"),
        ("2025-04-10T03:25:18.672807", "10.04.2025"),
    ],
)
def test_get_date_correct(correct_date: str, expected: str) -> None:
    """
    Функция тестирование правильности преобразования даты
    :param correct_date: str    :param expected: str
    :return: None
    """
    assert get_date(correct_date) == expected


@pytest.mark.parametrize(
    "incorrect_date, expected",
    [
        ("", ""),
        ("2024-_3-11", "11.03.2024"),
        ("20_24-05-12T02:26:19.671407", ""),
        # ("", ""),
        # ("", ""),
        # ("", ""),
    ],
)
def test_get_date_incorrect(incorrect_date: str, expected: str) -> None:
    """
    Функция тестирования на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами
    :param incorrect_date: str        :param expected: str
    :return: None
    """
    assert get_date(incorrect_date) == expected
