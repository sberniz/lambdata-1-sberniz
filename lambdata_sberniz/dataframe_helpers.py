"""
Some functions to help cleaning and handling dataframes
"""
import pandas as pd
import numpy as np
import re

# Function to Split date columns into month/day/year


def splitdate(df):

    """
    Split All Date Datatype columns into separate month/day/year columns
    """

    X = df.copy()
    for item in X:
        if X[item].dtypes == '<M8[ns]':
            X[item+'_month'] = X[item].dt.month
            X[item+'_day'] = X[item].dt.day
            X[item+'_year'] = X[item].dt.year
    return X


def auto_date_convert(df):

    """
    Convert All Date Objects in dataframe to datetime format
    """
    pattern = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
    X = df.copy()
    for item in X:
        if(X[item].dtypes == 'O'):
            result = re.match(pattern, X[item][0])
        if(result):
            X[item] = pd.to_datetime(X[item], infer_datetime_format=True)
    return X


def list_to_column(list, col_name, df):
    """
    Takes a list and adds to a column in dataframe, user must provide
    list,column Name (col_name) and dataframe
    """
    X = df.copy()
    list_to_series = pd.Series(data=list)
    X[col_name] = list_to_series
    return X


def version():
    """
    Print Version of package
    """

    print("Version 0.11")
