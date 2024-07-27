from math import sqrt
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
import numpy as np
import itertools

# City coordinates
cities = {
    0: (30, 40),  # Depot 0
    1: (37, 52),  # Depot 1
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def solve_tsp_dynamic_programming(distances):
    n = len(distances)
    memo = {(1 << i, i): (0 if i == 0 else float('inf'), -1) for i in range(n)}
    for mask_size in range(2, n+1):
        for mask in itertools.filterfalse(lambda x: bin(x).count("1") != mask_size, range(1 << n)):
            for final in range(n):
                if not (mask & (1 << final)):
                    continue
                prev_mask = mask ^ (1 << final)
                memo[mask, final] = min((memo[prev_mask, last][0] + distances[last][final], last)
                                          for last in range(n) if mask & (1 << last))
    mask = (1 << n) - 1
    res, parent = min((memo[mask, i][0] + distances[i][0], i) for i in range(1, n))
    tour = [0]
    for i in range(n - 1):
        tour.append(parent)
        new_mask, parent = mask ^ (1 << parent), memo[mask, parent][1]
        mask = new_mask
    tour.append(0)
    return tour, res

city_indices = list(range(len(cities)))

# Create distance matrix
dist_matrix = [[euclidean_distance(i, j) for j in city_indices] for i in city_ids]


# Step 1: Cluster cities around the depots
coordinates = np.array([cities[i] for i in cities])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(coordinates)
labels = kmeans.labels_

robot_0_cities = [i for i, label in enumerate(labels) if label == 0]
robot_1_cities = [i for i, label in enumerate(labels) if label == 1]

# Ensure depots are correctly assigned
if 0 not in robot_0_cities:
    robot_0_cities.append(0)
    robot_1_cities.remove(0)
if 1 not in robot_1_cities:
    robot_1_cities.append(1)
    robot_0_cities.remove(1)

# Step 2 and 3: Solve TSP for each robot
robot_0_distances = np.array([[dist_matrix[i][j] for j in robot_0_cities] for i in robot_0_cities])
robot_0_tour, robot_0_cost = solve_tsp_dynamic_programming(robot_0_distances)
robot_1_distances = np.array([[dist_matrix[i][j] for j in robot_1_cities] for i in robot_1_cities])
robot_1_tour, robot_1_cost = solve_tsp_dynamic_programming(robot_1_distances)

# Step
robot_0_full_tour = [robot_0_cities[i] for i in robot_0_tour]
robot_1_full_tour = [robot_1_cities[i] for i in robot_1_tour]

print("Robot 0 Tour:", robot_0_full_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)

print("Robot 1 Tour:", robot_1_full_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)

overall_cost = robot_0_cost + robot_1_cost
print("Overall Total Travel Cost:", overall_cost)