# mod_9

Учебный проект серверная часть виджета банковских операций клиента
***

### Описание модулей

1. Модуль "masks" предоставляет функции для маскировки номеров банковских карт и счетов.
2. Модуль "widget" предоставляет функции для обработки информации как о картах, так и о счетах.
3. Модуль "processing" содержит новые функции обработки данных по ключу и сортировки по дате.
4. Модуль `main` запускает все вышеперечисленные модули.

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
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> None:
    print(mask_account_card("Maestro 1596837868705199"))

    print(mask_account_card("Счет 64686473678894779589"))

    print(mask_account_card("MasterCard 7158300734726758"))

    print(mask_account_card("Счет 35383033474447895560"))

    print(mask_account_card("Visa Classic 6831982476737658"))

    print(mask_account_card("Visa Platinum 8990922113665229"))

    print(mask_account_card("Visa Gold 5999414228426353"))

    print(mask_account_card("Счет 73654108430135874305"))

    print(get_date("2024-03-11T02:26:18.671407"))

    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )


if __name__ == "__main__":
    main() 
```

#### Результат работы

Maestro 1596 83** **** 5199  
Счет \*\*9589  
MasterCard 7158 30** **** 6758  
Счет \*\*5560  
Visa Classic 6831 98** **** 7658  
Visa Platinum 8990 92** **** 5229  
Visa Gold 5999 41** **** 6353  
Счет \*\*4305  
11.03.2024  
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},   
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},  
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

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
- Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:  
`pytest --cov`  — при активированном виртуальном окружении.  
`poetry run pytest --cov` — через poetry.  
`pytest --cov=src --cov-report=html` — чтобы сгенерировать отчет о покрытии в HTML-формате.   
    где `src` — пакет c модулями, которые тестируем.   
Отчёт будет сгенерирован в папке `htmlcov` и храниться в файле с названием `index.html`.

- Oтчёт в HTML будет выглядеть следующим образом:  

![img.png](img.png)  
Произведены позитивные и негативные тесты для всех функций модулей `masks`, `widget` и `processing`.  
Тестами покрыто 100% кода

---

### Документация и ссылки
При необходимости установите [PyCharm Community Edition
](https://www.jetbrains.com/pycharm/download/)


---

### Лицензия

---

