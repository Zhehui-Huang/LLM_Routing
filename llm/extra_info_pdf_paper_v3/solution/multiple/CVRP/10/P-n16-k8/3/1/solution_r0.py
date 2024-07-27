import math
from sklearn.cluster import KMeans
import numpy as np

# Coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Demand of each city
demand = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# Number of robots and their capacity
num_robots = 8
capacity = 35

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Helper function to calculate the cost of a single route
def route_cost(route):
    cost = 0.0
    for i in range(len(route) - 1):
        cost += euclidean_distance(route[i], route[i + 1])
    return cost

# Clustering cities based on their locations to form initial clusters, using KMeans
coords = np.array([coord for coord in cities.values()])
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords[1:])
labels = kmeans.labels_

tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots

# Assigning cities to the nearest available robot
city_indices = list(cities.keys())[1:]  # Excluding the depot initially
for index, label in zip(city_indices, labels):
    if current_loads[label] + demand[index] <= capacity:
        tours[label].append(index)
        current_loads[label] += demand[index]

# Append the depot city as the start and end point
tours = [[0] + tour + [0] for tour in tours]

# Output the results
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost_val = route_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(tour_cost_val, 2)}")
    total_cost += tour_cost_val

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")