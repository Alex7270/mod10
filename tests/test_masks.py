import pytest

from src.masks import get_mask_account, get_mask_card_number

c = "Введен некорректный номер карты"
a = "Введен некорректный номер счета"


@pytest.mark.parametrize(
    "card_number_correct, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number_correct(card_number_correct: str, expected: str) -> None:
    """
    Функция тестирования правильности маскирования номера карты
    :param card_number_correct: str     :param expected:
    :return: None
    """
    assert get_mask_card_number(card_number_correct) == expected


@pytest.mark.parametrize(
    "card_number_incorrect, expected",
    [
        ("", c),
        ("1596837868705199555", c),
        ("1596837868", c),
        ("ff ff_______oooo", c),
        ("hh hha__ayy_my-r", c),
        ("55555gggIIII1228", c),
    ],
)
def test_get_mask_card_number_incorrect(card_number_incorrect: str, expected: str) -> None:
    """
    Функция тестирования правильности ввода номера карты
    :param card_number_incorrect: str    :param expected: str
    :return: None
    """
    assert get_mask_card_number(card_number_incorrect) == expected


@pytest.mark.parametrize(
    "account_number_correct, expected",
    [("64686473678894779589", "**9589"), ("35383033474447895560", "**5560"), ("73654108430135874305", "**4305")],
)
def test_get_mask_account_correct(account_number_correct: str, expected: str) -> None:
    """
    Функция тестирования правильности маскирования номера счета
    :param account_number_correct:      :param expected: str
    :return: None
    """
    assert get_mask_account(account_number_correct) == expected


@pytest.mark.parametrize(
    "account_number_incorrect, expected",
    [
        ("", a),
        ("6468647367889477958977888", a),
        ("1596837868", a),
        ("1359 _______oooo  44", a),
        ("hhhh____k kkk//  1234", a),
        ("55555gggIIII1228  --", a),
    ],
)
def test_get_mask_account_incorrect(account_number_incorrect: str, expected: str) -> None:
    """
    Функция тестирования правильности ввода номера счета
    :param account_number_incorrect:      :param expected: str
    :return: None
    """
    assert get_mask_account(account_number_incorrect) == expected
