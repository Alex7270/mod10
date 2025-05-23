from typing import Any

import pandas as pd


def read_transaction_csv(path: str, row: int = 2) -> Any:
    """
    Чтение csv файла
    :param path: str
    :param row: int
    :return: Any
    """
    try:
        df = pd.read_csv(path, delimiter=";").head(row)
        return df.to_dict(orient="records")
    except Exception as e:
        return f"Error: {e}"


def read_transaction_xlsx(path: str, row: int = 2) -> Any:
    """
    Чтение xlsx файла
    :param path: str
    :param row: int
    :return: Any
    """
    try:
        df = pd.read_excel(path).head(row)
        return df.to_dict(orient="records")
    except Exception as e:
        return f"Error: {e}"
