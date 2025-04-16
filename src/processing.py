def filter_by_state(my_list: list[dict[str, int | str]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """
    Функция фильтрует входной список по ключу
    """
    return [my_dict for my_dict in my_list if my_dict.get("state") == state]
