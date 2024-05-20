#!/usr/bin/python3
import pandas as pd

def df_convert_column_to_datetime(df, column_name='Date'):
    df[column_name] = pd.to_datetime(df[column_name])
    return df


def df_aggregate_by_month(df, value_column, method='sum', date_column='Date'):
    result = df.groupby(df[date_column].dt.to_period('M'))[value_column].agg(method).to_frame()
    result = result.reset_index()
    result = result.set_index(['Date'])
    print(type(result))
    print(result.columns)
    return result


def df_aggregate_by_quarter(df, value_column, method='sum', date_column='Date'):
    result = df.groupby(df[date_column].dt.to_period('Q'))[value_column].agg(method).to_frame()
    result = result.reset_index()
    result = result.set_index(['Date'])
    print(type(result))
    print(result.columns)
    return result
    return
