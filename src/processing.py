from datetime import datetime
from typing import Any


def filter_by_state(my_list: list[dict[str, int | str]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """
    Функция фильтрует входной список по ключу
    :param my_list: list[dict[str, int | str]
    :param state: str
    :return: list[dict[str, int | str]]
    """
    return [my_dict for my_dict in my_list if my_dict.get("state") == state]


def sort_by_date(list_dict: list[dict[str, Any]], sort: bool = True) -> list[dict[str, Any]] | str:
    """
    Функция сортирует список по дате
    """
    new_list_dict = []
    for my_dict in list_dict:
        try:
            datetime.strptime(str(my_dict.get('date'))[:10], "%Y-%m-%d")
        except Exception:
            return "Ошибка формата даты"
        else:
            new_list_dict.append(my_dict)

    return sorted(new_list_dict, key=lambda x: str(x.get("date")), reverse=sort)
