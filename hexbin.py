# This is a DataQuest Jupyter project with details here:
# https://www.dataquest.io/m/146/guided-project%3A-visualizing-earnings-based-on-college-majors
# the dataset was from recent-grads.csv on github: https://github.com/fivethirtyeight/data/tree/master/college-majors

import pandas as pd
import matplotlib.pyplot as plt

# Initialise dataset
recent_grads = pd.read_csv("recent-grads.csv", delimiter=",")
first_row = recent_grads.iloc[0]
# print(recent_grads.head())
# print(recent_grads.tail())
summary_stats = recent_grads.describe()

# Clean dataset - drop rows with missing values
raw_data_count = recent_grads.shape
# print(raw_data_count)
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape
# print(cleaned_data_count)

# hexbin plots https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hexbin.html
recent_grads.plot(x='Women', y='Unemployment_rate', kind='hexbin', gridsize=10, cmap="viridis")

plt.show()