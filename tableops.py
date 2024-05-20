#!/usr/bin/python3
import pandas as pd


def df_convert_column_to_datetime(df, column_name='Date', dayfirst=False):
    df[column_name] = pd.to_datetime(df[column_name], dayfirst=dayfirst)
    return df


def df_aggregate_by_month(df, value_column, method='sum', date_column='Date'):
    if isinstance(value_column, str) and isinstance(method, str):
        result = df.groupby(df[date_column].dt.to_period('M'))[value_column].agg(method).to_frame()
    elif isinstance(value_column, list) and isinstance(method, list):
        result = df.groupby(df[date_column].dt.to_period('M')).agg({v:m for (v,m) in zip(value_column, method)})
    else:
        raise TypeError("'value_column' and 'method' arguments both have to be strings or both have to be lists")
    result = result.reset_index()
    result = result.set_index(['Date'])
    return result


def df_aggregate_by_quarter(df, value_column, method='sum', date_column='Date'):

    if isinstance(value_column, str) and isinstance(method, str):
        result = df.groupby(df[date_column].dt.to_period('Q'))[value_column].agg(method).to_frame()
    elif isinstance(value_column, list) and isinstance(method, list):
        result = df.groupby(df[date_column].dt.to_period('Q')).agg({v:m for (v,m) in zip(value_column, method)})
    else:
        raise TypeError("'value_column' and 'method' arguments both have to be strings or both have to be lists")
    result = result.reset_index()
    result = result.set_index(['Date'])
    return result
