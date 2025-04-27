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


@pytest.fixture
def correct_date() -> list[str]:
    return [
        "2024-03-11T02:26:18.671407",
        "2024-05-12T02:26:19.671407",
        "2025-04-10T03:25:18.672807",
        "2025-12-31T03:25:18.672807",
        "2025-01-01T03:25:18.672807",
        "2024-02-29T03:25:18.672807",
    ]


@pytest.fixture
def incorrect_date() -> list[str]:
    return [
        "",
        "2024-_3-11",
        "20_24-05-12T02:26:19.671407",
        "2025-05-32T02:26:19.6714",
        "2025-13-22T02:26:19.671407",
        "2024-02-30T02:26:19.671407",
    ]


@pytest.fixture
def my_list() -> list[dict[str, int | str]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def user_list() -> tuple[list[dict[str, int | str]], list[str]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], ["CANCELED", "EXECUTED"]


@pytest.fixture
def test_sort_by_date_default() -> list[dict[str, int | str]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_sort_by_date() -> tuple[list[dict[str, int | str]], bool]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], False
