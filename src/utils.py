import json
from typing import Any


def get_transaction(path: str) -> list[dict[str, Any]] | Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path: str
    :return: list[dict[str, Any] | Any]
    """
    try:
        with open(path, encoding="utf-8") as f:
            data_list = json.load(f)
            if len(data_list) in [0, 1] or not data_list[0]:
                return []
            else:
                return data_list
    except (FileNotFoundError, json.JSONDecodeError):
        return []
