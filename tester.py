# Import necessary modules and libraries
import unittest
import pandas as pd
from lambdata_sberniz.dfhelper import df_manager
"""Tester is for df_manager unittest of the functions"""
# Test Dataset
df = pd.read_csv('https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Applied-Modeling/master/data/apartments/renthop-nyc.csv')


class dfmanagerTests(unittest.TestCase):
    """Test the df_manager class with unit tests"""

    def test_convert(self):
        """Tests the convert function make sure final dtype is 'datetime'"""
        df1 = df_manager(df)
        dtype = '<M8[ns]'
        df1.date_convert()
        self.assertEqual(df1.df['created'].dtypes, dtype)

    def test_split_date(self):
        """Makes sure after the split, there are additionally 3 columns"""
        df1 = df_manager(df)
        df1.date_convert()
        len_prior = df1.df.shape[1]
        df1.split_date()
        len_after = df1.df.shape[1]
        self.assertEqual(len_prior + 3, len_after)

    def test_split_date_column_name(self):
        """makes sure the correct names for the columns where created"""
        df1 = df_manager(df)
        df1.date_convert()
        df1.split_date()
        names = ['created_month', 'created_day', 'created_year']
        for item in names:
            self.assertIn(item, df1.df.columns)

if __name__ == '__main__':
    # Conditional statement, only when file is run not when imported
    unittest.main()
