#! /usr/bin/python
# src: https://www.pythonforengineers.com/data-analysis-with-pandas/
import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile("Obes-phys-acti-diet-eng-2014-tab.xls")
# Define the columns to be read
columns1 = ["year", "total", "males", "females"]
data_gender = data.parse(u"7.1", skiprows=4, skipfooter=14, names=columns1)
# Remove the N/A from the data
data_gender.dropna(inplace=True)
data_gender.set_index("year", inplace=True)

# 2nd approach
data_age = data.parse('7.2', skiprows=4, skipfooter=14)
# Rename Unnamed to year
data_age.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
# Remove the N/A from the data
data_age.dropna(inplace=True)
data_age.set_index('Year', inplace=True)
# Plotting everything cause total to override everything
data_age_minus_total = data_age.drop('Total', axis=1)


# Plot all
# data_gender.plot()
# data_age.plot()
# data_age_minus_total.plot()

# Children vs adults
data_age['Under 16'].plot(label='Under 16')
data_age["25-34"].plot(label="25-34")
plt.legend(loc="upper right")
plt.show()

