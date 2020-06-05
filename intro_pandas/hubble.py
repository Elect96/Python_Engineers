#! /usr/bin/python
# https://www.pythonforengineers.com/introduction-to-pandas/import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hubble_data.csv")
data.head()
data.set_index("distance", inplace=True)
data.plot()
plt.show()

# no headers .csv handling
# headers = ["dist", "rec_vel"]
# data_no_headers = pd.read_csv("hubble_data_no_headers.csv", names=headers)
# data_no_headers.set_index("dist", inplace=True)
# data_no_headers.plot()
# plt.show()

