import logging

# создаем именной логер
logger = logging.getLogger(__name__)

# создаем хендлер для вывода логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")

# создаем форматер
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")

# устанавливаем форматер для хендлера
file_handler.setFormatter(file_formatter)

# добавляем хендлер в логер
logger.addHandler(file_handler)

# устанавливаем уровень логирования
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция маскировки номера банковской карты
    """
    if len(card_number) == 16 and card_number.isdigit():
        logger.info("маскировки номера карты OK")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.error("Введен некорректный номер карты")
    return "Введен некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """
    Функция маскировки номера банковского счета
    """
    if len(account_number) == 20 and account_number.isdigit():
        logger.info("маскировки номера счета OK")
        return f"**{account_number[-4:]}"
    logger.error("Введен некорректный номер счета")
    return "Введен некорректный номер счета"
