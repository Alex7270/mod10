# mod_9

Учебный проект серверная часть виджета банковских операций клиента
***

### Описание модулей

1. Модуль "masks" предоставляет функции для маскировки номеров банковских карт и счетов.
2. Модуль "widget" предоставляет функции для обработки информации как о картах, так и о счетах.
3. Модуль "processing" содержит новые функции обработки данных по ключу и сортировки по дате.
4. Модуль "generators" содержит функции для работы с массивами транзакций.  
5. Модуль "read_transactions" предоставляет функции для считывания финансовых операций из CSV- и XLSX-файлов.
6. Модуль "decorators" обеспечивает более глубокий контроль и анализ поведения программы в процессе ее выполнения.  
7. В модулях "utils" и "external_api" реализован функционал конвертации валютю.  
8. В модуле "filters" реализована функция для поиска в списке словарей операций по заданной строке.  
9. Модуль "countings" предоставляет функцию для подсчета количества банковских операций определенного типа.  
10. модуле "main" отвечает за основную логику проекта и связывает функциональности между собой.

---

### Установка и использование

- Установите [Python](https://www.python.org/downloads/)
- Установить менеджер пакетов poetry при помощи pip:

```
pip install poetry
```

- Клонируйте проект с репозитория GitHub:

```
git clone https://github.com/Alex7270/mod10.git
```

- Установите зависимости:

```
poetry update
```

- Запустите main.py:

```
python main.py
```

***

### Примеры использования

```Python 
from typing import Any

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
            transaction_sort: list[dict[str, Any]] | str = sort_by_date(transaction_state)
        else:
            transaction_sort = sort_by_date(transaction_state, False)
    else:
        transaction_sort = sort_by_date(transaction_state)

    user_answer_5 = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if user_answer_5 == "да" and user_answer == "1":
        transaction_sort_rub = list(filter_by_currency(transaction_sort,"RUB"))
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

    print("\nРаспечатываю итоговый список транзакций...")

    count = len(transactions_filter)
    description = transaction_descriptions(transactions_filter)

    print(f"\nВсего банковских операций в выборке: {count}\n")

    for i in transactions_filter:
        date = get_date(str(i.get("date")))
        account_card_1 = mask_account_card(str(i.get("from"))) if str(i.get("from")) not in ["nan", "None"] else ""
        account_card_2 = mask_account_card(str(i.get("to")))

        amount = str(i.get("operationAmount", "").get("amount", "")) if user_answer == "1" else str(i.get("amount"))
        currency_code = (
            i.get("operationAmount", {}).get("currency").get("code")
            if user_answer == "1"
            else str(i.get("currency_code"))
        )

        print(
            f"{date} {next(description)}\n{account_card_1} "
            f"-> {account_card_2}\nСумма: {int(float(amount))} {currency_code}\n"
        )

    return None


if __name__ == "__main__":
    main()

```

#### Результат работы

       Привет! Добро пожаловать в программу работы с банковскими транзакциями.  
    Выберите необходимый пункт меню:  

        1. Получить информацию о транзакциях из JSON - файла  
        2. Получить информацию о транзакциях из CSV - файла  
        3. Получить информацию о транзакциях из XLSX - файла  

    Выберете пункт: 1  
Для обработки выбран JSON-файл.  

        Введите статус, по которому необходимо выполнить фильтрацию.  
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING  

        Введите статус: EXECUTED  
Операции отфильтрованы по статусу EXECUTED  
Отсортировать операции по дате? Да/Нет:   
Выводить только рублевые транзакции? Да/Нет:   
Отфильтровать список транзакций по определенному слову в описании? Да/Нет:  

Распечатываю итоговый список транзакций...  

Всего банковских операций в выборке: 85  

08.12.2019 Открытие вклада  
 -> Счет **5907  
Сумма: 41096 USD  

07.12.2019 Перевод организации  
Visa Classic 2842 87** **** 9012 -> Счет **3655  
Сумма: 48150 USD  

19.11.2019 Перевод организации  
Maestro 7810 84** **** 5568 -> Счет **2869  
Сумма: 30153 RUB  

13.11.2019 Перевод со счета на счет  
Счет **9794 -> Счет **8125  
Сумма: 62814 RUB  

05.11.2019 Открытие вклада  
 -> Счет **8381  
Сумма: 21344 RUB  


***

### Тестирование

- Установите через `Poetry` `Pytest`:

```commandline
poetry add --group dev pytest
``` 

- Установите библиотеку `pytest-cov`:

```commandline
poetry add --group dev pytest-cov
```
- Установите библиотеку `requests`:
```commandline
poetry add requests
```
- Установите библиотеку python-dotenv:
```commandline
poetry add python-dotenv
```
- Установите библиотеку pandas:
```commandline
poetry add pandas
```


- Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:  
  `pytest --cov`  — при активированном виртуальном окружении.  
  `poetry run pytest --cov` — через poetry.  
  `pytest --cov=src --cov-report=html` — чтобы сгенерировать отчет о покрытии в HTML-формате.   
  где `src` — пакет c модулями, которые тестируем.   
  Отчёт будет сгенерирован в папке `htmlcov` и храниться в файле с названием `index.html`.

- Oтчёт в HTML будет выглядеть следующим образом:

![img.png](img.png)    
Произведены позитивные и негативные тесты для всех функций модулей `masks`, `widget`,`processing`,`generators`, `decorators`, `utils`, `external_api`, `read_transactions`, `filters`, `countings` .   
Тестами покрыто 99% кода

---

### Документация и ссылки

При необходимости установите [PyCharm Community Edition
](https://www.jetbrains.com/pycharm/download/)


---

### Лицензия

---

