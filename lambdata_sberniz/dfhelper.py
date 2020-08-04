import pandas as pd
import numpy as np
import re


class df_manager:
    """DataFrame Mini Manager"""
    def __init__(self, df):
        self.df = df

    def date_convert(self):
        """Convert dates to date object"""
        pattern = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
        for item in self.df:
            if(self.df[item].dtypes == 'O'):
                result = re.match(pattern, self.df[item][0])
                if(result):
                    self.df[item] = pd.to_datetime(
                        self.df[item], infer_datetime_format=True)

    def split_date(self):
        """Split Date into month/day/year"""
        for item in self.df:
            if self.df[item].dtypes == '<M8[ns]':
                self.df[item+'_month'] = self.df[item].dt.month
                self.df[item+'_day'] = self.df[item].dt.day
                self.df[item+'_year'] = self.df[item].dt.year

    def senddf(self):
        """Sends back the df to variable"""
        return self.df

    def __repr__(self):
        return 'data_management_class'


def list_to_column(list, col_name, df):
    """
    Takes a list and adds to a column in dataframe, user must provide
    list,column Name (col_name) and dataframe
    """
    X = df.copy()
    list_to_series = pd.Series(data=list)
    X[col_name] = list_to_series
    return X
