import matplotlib.pyplot as plt
import numpy as np
import pandas

csv_file = pandas.read_csv("data.csv")
paloma = csv_file["Paloma Score"].values.tolist()
episodes = range(len(paloma))

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.scatter(episodes, paloma)                    # Plot some data on the Axes.
plt.show()                           # Show the figure.