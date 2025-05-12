import os
from datetime import datetime
from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    """
    Функция тестирования декоратора log при отсутствии параметров и вывода результатов в консоль
    """

    @log()
    def add_numbers(a: float, b: float) -> float:
        return a + b

    add_numbers(2, 3)
    captured = capsys.readouterr()
    assert (
        captured.out == f"\nНачало работы функции: {datetime.now().strftime('%Y-%m-%d %X')}\n\n"
        f"Имя функции: add_numbers\nNone\n"
        f"Аргументы функции args: (2, 3); kwargs: {{}}\n\n"
        f"Окончание работы функции: {datetime.now().strftime('%Y-%m-%d %X')}\n\n"
        f"Результат работы функции ОК: \n5\n\n"
    )


def test_log_param() -> None:
    """
    Функция тестирования декоратора log при наличии параметров и записи результатов в файл
    """

    @log(filename="mylog2.txt")
    def add_numbers(a: float, b: float) -> float:
        return a + b

    add_numbers(2, 3)

    try:
        # Проверяем содержимое файла mylog.txt
        with open("data/mylog2.txt", "r", encoding="utf-8") as file:
            logs = file.read()
            assert (
                f"\nНачало работы функции: {datetime.now().strftime('%Y-%m-%d %X')}\n\n"
                f"Имя функции: add_numbers\nNone\n"
                f"Аргументы функции args: (2, 3); kwargs: {{}}\n\n"
                f"Окончание работы функции: {datetime.now().strftime('%Y-%m-%d %X')}\n\n"
                f"Результат работы функции ОК: \n5\n"
            ) in logs

    finally:
        pass
        # Удаляем временный файл
        os.remove("data/mylog2.txt")


"""Этот код создаёт временный файл, использует его для логирования,
проверяет содержимое файла и затем удаляет его.
Убедись, что путь к твоему декоратору и функции указан правильно.
"""

# import tempfile
# import os
# from your_module import log, my_function  # Импортируй свой декоратор и функцию
#
#
# # Тестовая функция
# @log(filename="test_log.txt")
# def test_function(x, y):
#     return x + y
#
#
# # Тестирование с временным файлом
# with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#     filename = temp_file.name
#
# try:
#     # Применяем декоратор с временным файлом
#     @log(filename=filename)
#     def test_function(x, y):
#         return x + y
#
#
#     # Вызываем функцию
#     test_function(1, 2)
#
#     # Проверяем содержимое временного файла
#     with open(filename, 'r') as file:
#         logs = file.read()
#         assert "test_function ok" in logs
# finally:
#     # Удаляем временный файл
#     os.remove(filename)


"""для тестирования функции, создающей файл txt, можно использовать
временные файлы с помощью модуля tempfile. Проверь, что файл создается
и содержит ожидаемые данные, а затем удали его после теста.
Также можешь использовать pytest с фикстурой tmp_path для работы с временными файлами.
"""

# import os
#
# def test_create_txt_file(tmp_path):
#     file_path = tmp_path / "test.txt"
#     file_path.write_text("test content")
#     assert file_path.read_text() == "test content"
#     assert os.path.exists(file_path)
