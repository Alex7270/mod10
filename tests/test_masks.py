from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"
    assert get_mask_card_number("1596837868705199555") == "Введен некорректный номер карты"
    assert get_mask_card_number("159683786") == "Введен некорректный номер карты"
    assert get_mask_card_number("") == "Введен некорректный номер карты"


def test_get_mask_account() -> None:
    assert get_mask_account("64686473678894779589") == "**9589"
    assert get_mask_account("6468647367889477958977888") == "Введен некорректный номер счета"
    assert get_mask_account("64686473678") == "Введен некорректный номер счета"
    assert get_mask_account("") == "Введен некорректный номер счета"
