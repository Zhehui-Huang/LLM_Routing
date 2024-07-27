import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Function to compute the total tour distance
def tour_distance(tour, cities):
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Cluster cities into clusters equal to the number of robots
coordinates = np.array(cities[1:])  # exclude the depot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Function to solve the TSP using simple permutations (feasible for small problem size)
def solve_tsp(cities):
    min_dist = float('inf')
    best_tour = None
    all_permutations = permutations(range(len(cities)))
    for perm in all_permutations:
        dist = tour_distance([0] + list(perm) + [0], cities)
        if dist < min_dist:
            min_dist = dist
            best_tour = [0] + list(perm) + [0]
    return best_tour, min_dist

# Assign cities to each robot and solve TSP
tours = []
costs = []
for i in range(num_robots):
    assigned_cities = [0] + [index + 1 for index, label in enumerate(labels) if label == i]
    assigned_coords = [cities[index] for index in assigned_cities]
    tour, cost = solve_tsp(assigned_coords)
    tours.append([assigned_cities[j] for j in tour])
    costs.append(cost)

overall_cost = sum(costs)

# Output the tours and costs
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")