import json
import logging
from typing import Any

# создаем именной логер
logger = logging.getLogger(__name__)

# создаем хендлер для вывода логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w")

# создаем форматер
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")

# устанавливаем форматер для хендлера
file_handler.setFormatter(file_formatter)

# добавляем хендлер в логер
logger.addHandler(file_handler)

# устанавливаем уровень логирования
logger.setLevel(logging.DEBUG)


def get_transaction(path: str) -> list[dict[str, Any]] | Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path: str
    :return: list[dict[str, Any] | Any]
    """
    try:
        logger.info("ok")
        with open(path, encoding="utf-8") as f:
            data_list = json.load(f)
            return data_list
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        logger.error(f"{e}")
        return []
