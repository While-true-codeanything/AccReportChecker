import re

import numpy as np
import pandas as pd


def parse_number(text):
    if not isinstance(text, str):
        text = str(text)
    match = re.search(r'\d{7,8}', text)
    if match:
        return int(match.group())
    else:
        print("Error. Not Found. Unsupported Format")
        print(text)
        exit(1)


epsilon = 1e-5


def check_row(row):
    if (pd.isnull(row['total_sum_df']) and row['total_sum_df2'] == 0) or (pd.isnull(row['total_sum_df2']) and row['total_sum_df'] == 0):
        return np.nan
    elif pd.isnull(row['total_sum_df']):
        return f"id {int(row['id'])} отсутствует в первом из файлов. Значение во втором {row['total_sum_df2']}"
    elif pd.isnull(row['total_sum_df2']):
        return f"id {int(row['id'])} отсутствует во втором из файлов. Значение в первом {row['total_sum_df']}"
    elif abs(row['total_sum_df'] - row['total_sum_df2']) > epsilon:
        return (f"id {int(row['id'])}, значение в первом файле: {row['total_sum_df']}, "
                f"значение во втором файле: {row['total_sum_df2']}")
    return np.nan
