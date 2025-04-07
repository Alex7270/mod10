from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """
    Функция маскировки номера банковской карты или счета
    """
    number_lst = number.strip().split(" ")

    if number_lst[0].lower() == "счет":
        return f"{number_lst[0]} {get_mask_account(number_lst[1])}"
    elif len(number_lst) > 2:
        return f"{' '.join(number_lst[:2])} {get_mask_card_number(number_lst[2])}"
    else:
        return f"{number_lst[0]} {get_mask_card_number(number_lst[1])}"


def get_date(date: str) -> str:
    """
    Функция преобразования формата даты
    """
    date_str = date[:10]
    return datetime.strptime(date_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')
