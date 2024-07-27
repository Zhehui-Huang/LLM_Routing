import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import itertools
import random

# Constants Setup
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
               (58, 27), (37, 69)]
num_cities = len(coordinates)
num_robots = 8
depot = coordinates[0]
cities = coordinates[1:]

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def route_cost(route):
    return sum(euclidean_distance(coordinates[route[i]], coordinates[route[i+1]]) for i in range(len(route) - 1))

# Stage 1: Initialize Solutions with Fuzzy C-Means Clustering (using KMeans as an approximation)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
clusters = kmeans.labels_

# Generate initial robot tours from clusters
tours = [[] for _ in range(num_robots)]
for city_index, cluster_index in enumerate(clusters):
    tours[cluster_index].append(city_index + 1)   # city indices offset by 1 due to depot exclusion in cities

# Random Greedy Heuristic for initial tours
for tour in tours:
    random.shuffle(tour)  # Introduce randomness
    tour.insert(0, 0)    # Start at the depot
    tour.append(0)       # Return to the depot

# Stage 2: Optimization using VNS
# Implement simple 2-opt local search as an example of VNS
def two_opt(route):
    best_route = route
    best_cost = route_cost(route)
    for i in range(1, len(route) - 2):
        for j in range(i + 2, len(route)):
            if j - i == 1: continue  # these are adjacent already
            new_route = route[:i] + route[i:j][::-1] + route[j:]
            new_cost = route_cost(new_route)
            if new_cost < best_cost:
                best_route = new_reference
                best_cost = new_cost
    return best_route

# Apply 2-opt to each tour to find a better local solution
optimized_tours = [two_opt(tour) for tour in tours]

# Calculate costs
costs = [route_cost(tour) for tour in optimized_tours]
max_cost = max(costs)

# Print solutions
for i, tour in enumerate(optimized_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")