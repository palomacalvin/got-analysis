import matplotlib.pyplot as plt
import numpy as np
import pandas

csv_file = pandas.read_csv("data.csv")
paloma = csv_file["Paloma Score"].values.tolist()
jack = csv_file["Jack Score"].values.tolist()
episodes = range(len(paloma))

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.scatter(episodes, paloma)         # Plot some data on the Axes.
plt.show()                           # Show the figure.


# Bar graphs of:
# Avg. rating per season, totaled by all data

### Compute averages for all episodes by person
### todo: turn this into a function
avg_total_p = 0
avg_total_j = 0
count_p = 0
count_j = 0
track_p = 0
track_j = 0


for data in paloma:
    float(data)
    count_p += 1
    track_p += data

for data in jack:
    float(data)
    count_j += 1
    track_j += data

avg_total_p = track_p / count_p
avg_total_j = track_j / count_j

print(avg_total_p)
print(avg_total_j)

# BOX PLOTS TEST
fig, ax = plt.subplots()
VP = ax.boxplot(csv_file, widths=1.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 1.5})

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


### Create averages of ratings ///per season///


# Avg. rating per season, separated by rater


# Linear graph with highest and lowest rated eps. per season w/divergent colors


# Bar chart of the number of different level ratings by person and total


# PIE CHART TEST
fig, ax = plt.subplots()
ax.pie(paloma, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()



# Show which episodes were rated the same between raters