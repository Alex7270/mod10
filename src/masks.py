def get_mask_card_number(card_number: str) -> str:
    """
    Функция маскировки номера банковской карты
    """
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return "Введен некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """
    Функция маскировки номера банковского счета
    """
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"

    return "Введен некорректный номер счета"
