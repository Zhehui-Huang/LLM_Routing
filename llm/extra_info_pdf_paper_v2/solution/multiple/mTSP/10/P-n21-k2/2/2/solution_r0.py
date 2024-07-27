import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Define city coordinates (index 0 is the depot)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
num_robots = 2
depot = cities[0]

# Exclude the depot for clustering
cluster_cities = cities[1:]

# K-Means clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cluster_cities)
labels = kmeans.labels_

# Function to calculate the total travel cost
def calculate_tour_cost(tour, cities):
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Organizing tours for each robot
tours = [[] for _ in range(num_robots)]
for idx, label in enumerate(labels):
    tours[label].append(idx + 1)

# Inserting depot at start and end of each tour
for tour in tours:
    tour.insert(0, 0)
    tour.append(0)

# Calculating costs
robot_costs = [calculate_tour_cost(tour, cities) for tour in tours]
overall_cost = sum(robot_costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")