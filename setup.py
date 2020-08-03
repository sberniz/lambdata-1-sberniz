"""
lambdata - a collection of datascience helper function
"""

import setuptools

REQUIRED = [
        "numpy",
        "pandas",
        "re"
        ]

with open("README.md","r") as file:
        LONG_DESCRIPTION = file.read()

setuptools.setup(
   name="lambdata-sberniz",
   version= "0.0.4",
   author="sberniz",
   description="a collection of data science helper functions",
   long_desription=LONG_DESCRIPTION,
   long_description_content_type="text/markdown",
   url="https://github.com/sberniz/lambdata-1-sberniz/",
   packages=setuptools.find_packages(),
   python_requires=">=3.6",
   install_requires=REQUIRED,
   classifier=[
       "Programming Language:: Python :: 3",
       "License:: NONE",
       "Operating System :: OS Independent",
       ],
   )
