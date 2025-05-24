from typing import Any

import pandas as pd


def read_transactions_csv(path: str) -> Any:
    """
    Чтение csv файла
    :param path: str   :return: Any
    """
    try:
        df = pd.read_csv(path, delimiter=";")
        df_lst = df.to_dict(orient="records")
        if len(df_lst) != 0:
            return df_lst
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def read_transactions_xlsx(path: str) -> Any:
    """
    Чтение xlsx файла
    :param path: str   :return: Any
    """
    try:
        df = pd.read_excel(path)
        df_lst = df.to_dict(orient="records")
        if len(df_lst) != 0:
            return df_lst
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
