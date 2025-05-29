def main() -> None:
    while True:
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
            print(
                """
            Для обработки выбран JSON-файл."""
            )
            break

        elif user_answer == "2":
            print(
                """
            Для обработки выбран CSV-файл."""
            )
            break

        elif user_answer == "3":
            print(
                """
            Для обработки выбран XLSX-файл."""
            )
            break
        else:
            print(
                """
            Некорректный ввод данных"""
            )

    while True:
        user_answer_2 = input(
            """
        Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n
        Введите статус: """
        ).upper()

        if user_answer_2 == "EXECUTED":
            print(
                f"""
            Операции отфильтрованы по статусу {user_answer_2}"""
            )
            break

        elif user_answer_2 == "CANCELED":
            print(
                f"""
            Операции отфильтрованы по статусу {user_answer_2}"""
            )
            break

        elif user_answer_2 == "PENDING":
            print(
                f"""
            Операции отфильтрованы по статусу {user_answer_2}"""
            )
            break
        else:
            print(
                f"""
            Статус операции {user_answer_2} недоступен."""
            )

    user_answer_3 = (
        input(
            """
        Отсортировать операции по дате? Да/Нет: """
        )
        .strip()
        .lower()
    )
    if user_answer_3 == "да":
        pass
    else:
        pass

    user_answer_4 = input(
        """
        Отсортировать по возрастанию или по убыванию?: """
    ).lower()
    if user_answer_4 == "по возрастанию":
        pass
    elif user_answer_4 == "по убыванию":
        pass
    else:
        pass

    user_answer_5 = input(
        """
        Выводить только рублевые транзакции? Да/Нет: """
    ).lower()
    if user_answer_5 == "да":
        pass
    elif user_answer_5 == "нет":
        pass
    else:
        pass

    user_answer_6 = input(
        """
        Отфильтровать список транзакций по определенному слову в описании? Да/Нет: """
    ).lower()
    if user_answer_6 == "да":
        user_answer_7 = input(
            """
        Введите слово: """
        )
    else:
        pass

    print("Распечатываю итоговый список транзакций...")

    print()


if __name__ == "__main__":
    main()
