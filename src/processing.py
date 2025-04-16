def filter_by_state(my_list: list[dict[str, int | str]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """
    Функция фильтрует входной список по ключу
    """
    return [my_dict for my_dict in my_list if my_dict.get("state") == state]


def sort_by_date(list_dict: list[dict[str, int | str]], sort: bool = True) -> list[dict[str, int | str]]:
    """
    Функция сортирует список по дате
    """
    return sorted(list_dict, key=lambda x: x["date"], reverse=sort)
