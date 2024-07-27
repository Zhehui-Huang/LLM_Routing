import math
from sklearn.cluster import KMeans
import numpy as np

# Definition of city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_distance(tour):
    # Calculate the travel cost for a given tour
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Perform clustering using KMeans to divide cities between the robots
coords = np.array([cities[i] for i in range(1, 19)])  # Ignoring the depot city for clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(coords)
labels = kmeans.labels_

# Assemble tours starting from the depot city
tours = [[0] for _ in range(2)]
for i in range(len(labels)):
    tours[labels[i]].append(i + 1)  # Adding 1 to align with the city keys, ignoring depot in clustering

# Finalize each tour by returning to the depot
for tour in tours:
    tour.append(0)

# Calculate travel cost for each tour
costs = [total_distance(tour) for tour in tours]
max_cost = max(costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Maximum Travel Cost: {max_cost}")