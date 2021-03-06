# This is a DataQuest Jupyter project with details here:
# https://www.dataquest.io/m/146/guided-project%3A-visualizing-earnings-based-on-college-majors
# the dataset was from recent-grads.csv on github: https://github.com/fivethirtyeight/data/tree/master/college-majors

import pandas as pd
import matplotlib.pyplot as plt
import pandas.plotting as pdplt

# Initialise dataset
recent_grads = pd.read_csv("recent-grads.csv", delimiter=",")
first_row = recent_grads.iloc[0]

# Clean dataset - drop rows with missing values
raw_data_count = recent_grads.shape
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape

# bar plots: compare the percentages of women (ShareWomen) from the first ten rows and last ten rows
recent_grads['ShareWomen'].head(10).plot(kind='bar')
recent_grads['ShareWomen'].tail(10).plot(kind='bar')

plt.show()