#! /usr/bin/python
# https://www.pythonforengineers.com/introduction-to-pandas/import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("wages_hours.csv", sep="\t")
data2 = data[["AGE", "RATE"]]
data_sorted = data2.sort_values(["AGE"])
data_sorted.set_index("AGE", inplace=True)

data_sorted.plot()
plt.show()
