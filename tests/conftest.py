import pytest


@pytest.fixture
def card_number_correct() -> list[str]:
    return ["1596837868705199", "7158300734726758", "6831982476737658", "8990922113665229", "5999414228426353"]


@pytest.fixture
def card_number_incorrect() -> list[str]:
    return ["", "1596837868705199555", "1596837868", "ff ff_______oooo", "hh hha__ayy_my-r", "55555gggIIII1228"]
