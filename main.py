from pprint import pprint

from src.filters import filter_transactions
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import read_transactions_csv, read_transactions_xlsx
from src.utils import get_transaction
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Отвечает за основную логику проекта и связывает функциональности между собой.
    """
    user_answer = input(
        """
        Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:\n
        1. Получить информацию о транзакциях из JSON - файла
        2. Получить информацию о транзакциях из CSV - файла
        3. Получить информацию о транзакциях из XLSX - файла\n
    Выберете пункт: """
    )

    if user_answer == "1":
        print("Для обработки выбран JSON-файл.")
        transaction_file = get_transaction("data/operations.json")

    elif user_answer == "2":
        transaction_file = read_transactions_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")

    elif user_answer == "3":
        transaction_file = read_transactions_xlsx("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Некорректный ввод данных")
        return None

    while True:
        user_answer_2 = input(
            """
        Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n
        Введите статус: """
        ).upper()
        if user_answer_2 in ["EXECUTED", "CANCELED", "PENDING"]:
            transaction_state = filter_by_state(transaction_file, user_answer_2)

            print(f"Операции отфильтрованы по статусу {user_answer_2}")
            break
        else:
            print(f"Статус операции {user_answer_2} недоступен.")

    user_answer_3 = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if user_answer_3 == "да":
        user_answer_4 = input("Отсортировать по возрастанию или по убыванию?: ").lower()
        if user_answer_4 == "по убыванию":
            transaction_sort = sort_by_date(transaction_state)
        else:
            transaction_sort = sort_by_date(transaction_state, False)
    else:
        transaction_sort = sort_by_date(transaction_state)

    user_answer_5 = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if user_answer_5 == "да" and user_answer == "1":
        transaction_sort_rub = list(filter_by_currency(transaction_sort, "RUB"))
    elif user_answer_5 == "да" and user_answer in ["2", "3"]:
        transaction_sort_rub = [x for x in transaction_sort if not not x and x.get("currency_code", "") == "RUB"]
    else:
        transaction_sort_rub = transaction_sort
    if len(transaction_sort_rub) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return None

    user_answer_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if user_answer_6 == "да":
        user_answer_7 = input("Введите слово: ")
        transactions_filter = filter_transactions(transaction_sort_rub, user_answer_7)
    else:
        transactions_filter = transaction_sort_rub

    print("Распечатываю итоговый список транзакций...")

    count = len(transactions_filter)
    description = transaction_descriptions(transactions_filter)

    print(f"\nВсего банковских операций в выборке: {count}\n")

    for i in transactions_filter:
        date = get_date(i.get("date"))
        account_card_1 = mask_account_card(i.get("from")) if str(i.get("from")) not in ["nan", "None"] else ""
        account_card_2 = mask_account_card(i.get("to"))

        amount = (
            i.get("operationAmount", {}).get("amount", "")
            if user_answer == "1" and user_answer_5 == "да"
            else i.get("amount")
        )
        currency_code = (
            i.get("operationAmount", {}).get("currency").get("code")
            if user_answer == "1" and user_answer_5 == "да"
            else str(i.get("currency_code"))
        )

        print(
            f"{date} {next(description)}\n{account_card_1} "
            f"-> {account_card_2}\nСумма: {int(float(amount))} {currency_code}\n"
        )
    pprint(transactions_filter)
    return None


if __name__ == "__main__":
    main()
