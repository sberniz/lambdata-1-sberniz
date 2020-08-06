# lambdata-1-sberniz

# Version 0.1.3 - Latest

Added Unit Tests file tester.py

# Version 0.1.2

Converted Functions to classes and methods

# Usage:

Import a dataframe, and then intantiate a df_manager class as follow:
 
df = df_manage(df)

This converts every date column in a dataframe into pandas datetime:

df.date_convert()

This splits every datetime column in dataframe into 3 more columns in the order of Month/day/Year

with the following names columnname_month,columnname_day,columnname_year

df.split_date()

this will send the dataframe to a variable. 
df = df.senddf()

Project Repo Unit 3 Sprint 1, Module 4

Simple pip Package, test package 

# PIP INSTALL COMMAND

pip install -i https://test.pypi.org/simple/ lambdata-sberniz

