# This is a DataQuest Jupyter project with details here:
# https://www.dataquest.io/m/146/guided-project%3A-visualizing-earnings-based-on-college-majors
# the dataset was from recent-grads.csv on github: https://github.com/fivethirtyeight/data/tree/master/college-majors

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Initialise dataset
recent_grads = pd.read_csv("recent-grads.csv", delimiter=",")
first_row = recent_grads.iloc[0]

# Clean dataset - drop rows with missing values
raw_data_count = recent_grads.shape
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape

# Grouped bar plots
fig = plt.figure(figsize=(20, 10))

barWidth = 0.25

# set height of bar
bars1 = recent_grads['Men'].head(10)
bars2 = recent_grads['Women'].head(10)

# set position of bar on X axis
r1 = np.arange(len(bars1)) + 0.55
r2 = [x + barWidth for x in r1]

#make the plot
plt.bar(r1, bars1, color='b', width=barWidth, edgecolor='white', label='Men')
plt.bar(r2, bars2, color='r', width=barWidth, edgecolor='white', label='Women')

plt.xlabel('group', fontsize=2)
fig.subplots_adjust(bottom=0.3)
plt.xticks([r + barWidth for r in range(len(bars1))], recent_grads['Major'].head(10), rotation=45)

plt.legend()
plt.show()

