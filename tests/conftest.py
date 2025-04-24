import pytest


@pytest.fixture
def card_number_correct() -> list[str]:
    return ["1596837868705199", "7158300734726758", "6831982476737658", "8990922113665229", "5999414228426353"]


@pytest.fixture
def card_number_incorrect() -> list[str]:
    return ["", "1596837868705199555", "1596837868", "ff ff_______oooo", "hh hha__ayy_my-r", "55555gggIIII1228"]


@pytest.fixture
def account_number_correct() -> list[str]:
    return ["64686473678894779589", "35383033474447895560", "73654108430135874305"]


@pytest.fixture
def account_number_incorrect() -> list[str]:
    return [
        "",
        "6468647367889477958977888",
        "1596837868",
        "1359 _______oooo  44",
        "hhhh____k kkk//  1234",
        "55555gggIIII1228  --",
    ]


@pytest.fixture
def correct_number() -> list[str]:
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


@pytest.fixture
def incorrect_number() -> list[str]:
    return [
        "",
        "Счет",
        "MasterCard",
        "Счет  35383__033474447895560",
        "Visa   Classic   6831982476737658",
        "Visa Platinum 89  90922113665229",
        "Visa Gold 59994---14228426353",
        " Счет 7365410  hhh8430135874305  ",
    ]
