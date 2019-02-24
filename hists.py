# This is a DataQuest Jupyter project with details here:
# https://www.dataquest.io/m/146/guided-project%3A-visualizing-earnings-based-on-college-majors
# the dataset was from recent-grads.csv on github: https://github.com/fivethirtyeight/data/tree/master/college-majors

import pandas as pd
import matplotlib.pyplot as plt

# Initialise dataset
recent_grads = pd.read_csv("recent-grads.csv", delimiter=",")
first_row = recent_grads.iloc[0]

# Clean dataset - drop rows with missing values
raw_data_count = recent_grads.shape
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape

# Generate histogram - Sample size
#recent_grads['Sample_size'].hist(bins=25, range=(0, 5000))

# Generate histogram - Median
#recent_grads['Median'].hist(bins=25, range=(0, 5000))

# Generate histogram - Employed
#recent_grads['Employed'].hist(bins=10, range=(0, 100000))

# Generate histogram - Full_time
#recent_grads['Full_time'].hist(bins=25, range=(0, 10000))

# Generate histogram - Unemployment_rate
recent_grads['Unemployment_rate'].hist(bins=25, range=(0, 0.2))

# Generate histogram - Men
# recent_grads['Men'].hist(bins=25, range=(0, 10000))

# Generate histogram - Women
# recent_grads['Women'].hist(bins=25, range=(0, 10000))

plt.show()