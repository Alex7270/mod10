from typing import Any
from unittest.mock import patch

from src.read_transactions import read_transactions_csv, read_transactions_xlsx


@patch("pandas.read_csv")
def test_read_transactions_csv_correct(
    mock_csv: Any, path_to_file_csv: str, expected_transaction_correct: list[dict[str, Any]]
) -> None:
    """
    Тестирование чтения транзакций из csv-файла
    :param path_to_file_csv: str
    :param expected_transaction_correct: list[dict[str, Any]]
    :return: None
    """
    mock_csv.return_value.to_dict.return_value = expected_transaction_correct
    assert read_transactions_csv(path_to_file_csv) == expected_transaction_correct
    mock_csv.assert_called_once_with(path_to_file_csv, delimiter=";")


# @patch("pandas.read_excel")
# def test_read_transactions_xlsx(mock_excel):
#     """Тест excel"""
#
#     mock_excel.return_value.to_dict.return_value = [{"test": "test"}, {"test2": "test2"}]
#     assert read_transactions_xlsx("data/transaction_excel.xlsx") == [{"test": "test"}, {"test2": "test2"}]
#     mock_excel.assert_called_once_with("data/transaction_excel.xlsx")
