import math
from sklearn.cluster import KMeans
import numpy as np

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance calculation using Euclidean formula
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize k-means clustering for initial city distribution to robots
kmeans = KMeans(n_clusters=2, random_state=0)
city_points = np.array(list(cities.values()))
kmeans.fit(city_points[1:])  # Exclude depot city for clustering

# Assign cities to clusters/robots
labels = kmeans.labels_

robots_tours = {0: [0], 1: [0]}
for i, label in enumerate(labels):
    city_idx = i + 1  # Offset for actual city indices (excluding depot)
    robots_tours[label].append(city_idx)

# Append the return to the depot city at the end of each robot tour
for robot in robots_tours:
    robots_tours[robot].append(0)

# Calculate the travel cost for each robot tour
def calculate_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

robot_costs = {}
for robot in robots_tours:
    cost = calculate_tour_cost(robots_tours[robot])
    robot_costs[robot] = cost
    print(f"Robot {robot} Tour: {robots_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

# Evaluate the maximum distance traveled by any robot
max_cost = max(robot_costs.values())
print(f"Maximum Travel Delivery Cost: {max_cost}")