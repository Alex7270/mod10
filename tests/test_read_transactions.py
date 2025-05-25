from typing import Any
from unittest.mock import patch

from src.read_transactions import read_transactions_csv, read_transactions_xlsx


@patch("pandas.read_csv")
def test_read_transactions_csv_correct(
    mock_csv: Any, path_to_file_csv: str, expected_transaction_correct: list[dict[str, Any]]
) -> None:
    """
    Тестирование функции чтения транзакций из csv-файла
    :param path_to_file_csv: str
    :param expected_transaction_correct: list[dict[str, Any]]
    :return: None
    """
    mock_csv.return_value.to_dict.return_value = expected_transaction_correct
    assert read_transactions_csv(path_to_file_csv) == expected_transaction_correct
    mock_csv.assert_called_once_with(path_to_file_csv, delimiter=";")


@patch("pandas.read_excel")
def test_read_transactions_xlsx(
    mock_excel: Any, path_to_file_excel: str, expected_transaction_correct: list[dict[str, Any]]
) -> None:
    """
    Тестирование функции чтения транзакций из xlsx-файла
    :param mock_excel: Any
    :param path_to_file_excel: str
    :param expected_transaction_correct: list[dict[str, Any]]
    :return: None
    """

    mock_excel.return_value.to_dict.return_value = expected_transaction_correct
    assert read_transactions_xlsx(path_to_file_excel) == expected_transaction_correct
    mock_excel.assert_called_once_with(path_to_file_excel)


def test_read_transactions_csv_incorrect() -> None:
    """
    Тестирование функции чтения транзакций из csv-файла с некорректным путем к файлу
    :return: None
    """
    assert read_transactions_csv(" ") == []


@patch("pandas.read_csv")
def test_read_transactions_csv_empty(mock_csv: Any, path_to_file_csv: str) -> None:
    """
    Тестирование функции чтения транзакций из csv-файла с отсутствующими данными
    :param: mock_csv: Any
    :param: path_to_file_csv: str
    :return: None
    """
    mock_csv.return_value.to_dict.return_value = []
    assert read_transactions_csv(path_to_file_csv) == []
    mock_csv.assert_called_once_with(path_to_file_csv, delimiter=";")


@patch("pandas.read_excel")
def test_read_transactions_xlsx_empty(mock_excel: Any, path_to_file_excel: str) -> None:
    """
    Тестирование функции чтения транзакций из xlsx-файла с отсутствующими данными
    :param: mock_excel: Any
    :param: path_to_file_excel: str
    :return: None
    """
    mock_excel.return_value.to_dict.return_value = []
    assert read_transactions_xlsx(path_to_file_excel) == []
    mock_excel.assert_called_once_with(path_to_file_excel)


def test_read_transactions_xlsx_incorrect() -> None:
    """
    Тестирование функции чтения транзакций из xlsx-файла с некорректным путем к файлу
    :return: None
    """
    assert read_transactions_xlsx(" ") == []
