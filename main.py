import pandas as pd
from support_functions import parse_number, check_row


def caluclate_errors(df, df2):
    df['id'] = df[0].apply(parse_number)
    df['total_sum'] = df[1]
    df = df[['id', 'total_sum']]
    df = df.groupby('id')['total_sum'].sum().reset_index()
    df2['id'] = df2[0].apply(parse_number)
    df2['total_sum'] = df2[1]
    df2 = df2[['id', 'total_sum']]
    df2 = df2.groupby('id')['total_sum'].sum().reset_index()

    merged_df = pd.merge(df, df2, on='id', how='outer', suffixes=('_df', '_df2'))
    wrong_ids = merged_df.apply(check_row, axis=1).dropna().tolist()

    merged_df['difference'] = merged_df['total_sum_df2'] - merged_df['total_sum_df']
    total_difference = max(df['total_sum'].sum(), df2['total_sum'].sum()) - min(df['total_sum'].sum(),
                                                                                df2['total_sum'].sum())
    return wrong_ids, total_difference
