import matplotlib.pyplot as plt
import numpy as np
import pandas

# Reads CSV file and creates lists of data for each rater
csv_file = pandas.read_csv("data.csv")
paloma = csv_file["Paloma Score"].values.tolist()
jack = csv_file["Jack Score"].values.tolist()
episodes = range(len(paloma))        # paloma and jack both have the exact same length

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.scatter(episodes, paloma)         # Plot some data on the Axes.
plt.show()                           # Show the figure.


# Create lists of ratings separated by season
s1_p = paloma[0:10]
s1_j = jack[0:10]

s2_p = paloma[10:20]
s2_j = jack[10:20]

s3_p = paloma[20:30]
s3_j = jack[20:30]

s4_p = paloma[30:40]
s4_j = jack[30:40]

s5_p = paloma[40:50]
s5_j = jack[40:50]

s6_p = paloma[50:60]
s6_j = jack[50:60]

s7_p = paloma[60:67]
s7_j = jack[60:67]

s8_p = paloma[67:73]
s8_j = jack[67:73]


# Function that can compute the avg rating per season
def compute_avg_season(season_list):
    count = 0
    track = 0
    for data in season_list:
        float(data)
        track += data
        count += 1
    return track / count


# Compute avg. ratings per season per person
# and put it into a new list
avg_season_rating_p = []
avg_season_rating_j = []

avg_season_rating_p.append(compute_avg_season(s1_p))
avg_season_rating_p.append(compute_avg_season(s2_p))
avg_season_rating_p.append(compute_avg_season(s3_p))
avg_season_rating_p.append(compute_avg_season(s4_p))
avg_season_rating_p.append(compute_avg_season(s5_p))
avg_season_rating_p.append(compute_avg_season(s6_p))
avg_season_rating_p.append(compute_avg_season(s7_p))
avg_season_rating_p.append(compute_avg_season(s8_p))

avg_season_rating_j.append(compute_avg_season(s1_j))
avg_season_rating_j.append(compute_avg_season(s2_j))
avg_season_rating_j.append(compute_avg_season(s3_j))
avg_season_rating_j.append(compute_avg_season(s4_j))
avg_season_rating_j.append(compute_avg_season(s5_j))
avg_season_rating_j.append(compute_avg_season(s6_j))
avg_season_rating_j.append(compute_avg_season(s7_j))
avg_season_rating_j.append(compute_avg_season(s8_j))

print("Average ratings by season, Paloma:", avg_season_rating_p)
print("Average ratings by season, Jack:", avg_season_rating_j)




### Compute averages for all episodes by person
### todo: turn this into a function?
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

print("Total average of all seasons, Paloma:", avg_total_p)
print("Total average of all seasons, Jack:", avg_total_j)

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


# Avg. rating per season, separated by rater
seasons = [1, 2, 3, 4, 5, 6, 7, 8]

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.scatter(seasons, avg_season_rating_p)         # Plot some data on the Axes.
plt.show()                           # Show the figure.

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.scatter(seasons, avg_season_rating_j)         # Plot some data on the Axes.
plt.show()                           # Show the figure.

# Linear graph with highest and lowest rated eps. per season w/divergent colors



# Finding unique values in each list

rating_vals_p = []
rating_vals_j = []

for rating in paloma:
    if rating not in rating_vals_p:
        rating_vals_p.append(rating)
    else:
        continue

for rating in jack:
    if rating not in rating_vals_j:
        rating_vals_j.append(rating)
    else:
        continue

rating_vals_p.sort()
rating_vals_j.sort()

print("All unique values within Paloma:", rating_vals_p)
print("All unique values within Jack:", rating_vals_j)

dict_vals_p = {}
dict_vals_j = {}

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

for el in rating_vals_p:
    dict_vals_p[el] = countX(paloma, el)
    
for el in rating_vals_j:
    dict_vals_j[el] = countX(jack, el)

print("Paloma dict:", dict_vals_p)
print("Jack dict:", dict_vals_j)


# Pie chart of the number of different level ratings by person and total
# PIE CHART TEST
# Note: the labels for the pie charts will be the keys of each dictionary
fig, ax = plt.subplots()
ax.pie(dict_vals_p.values(), radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

fig, ax = plt.subplots()
ax.pie(dict_vals_j.values(), radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


# Show which episodes were rated the same between raters
same_rating = []
episode_num = 0
length = len(jack)

for episode_num in range(length):
    if jack[episode_num] == paloma[episode_num]:
        same_rating.append(episode_num)

print("List of episode indices with the same rating from both raters:", same_rating)

# Create a pdf of all the plots to display them together