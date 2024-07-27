import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from itertools import permutations

# Define the cities and their coordinates
cities = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
])

num_robots = 4
depot = 0

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def total_route_distance(route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += calculate_distance(cities[route[i]], cities[route[i+1]])
    return total_dist

# K-Means Clustering to assign cities to robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])
labels = kmeans.labels_

# Generate tours using a Nearest Neighbor approach for each cluster
tours = {}
for i in range(num_robots):
    tours[i] = [depot]  # start each tour at the depot

for idx, label in enumerate(labels):
    city_idx = idx + 1  # city indices offset by 1 because 0 is the depot
    tours[label].append(city_idx)

# Ensure each tour ends back at the depot
for i in range(num_robots):
    tours[i].append(depot)

# Optimize tours using 2-opt heuristic for each robot
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # changes nothing, skip then
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if total_route_distance(new_route) < total_route_distance(best):
                    best = new_route
                    improved = True
        route = best
    return best

for i in range(num_robots):
    tours[i] = two_opt(tours[i])

# Calculate distances and prepare output
costs = {}
for i in tours:
    costs[i] = total_route_distance(tours[i])

# Print results
max_cost = max(costs.values())
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")