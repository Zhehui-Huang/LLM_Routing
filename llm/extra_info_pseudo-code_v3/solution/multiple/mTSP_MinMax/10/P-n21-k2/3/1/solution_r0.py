import numpy as np
from sklearn.cluster import KMeans
import itertools

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance
def distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Clustering cities into two groups
xy = np.array(cities[1:])  # Exclude the depot for clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(xy)
labels = kmeans.labels_

# Creating initial routes for the two robots based on clusters
routes = {0: [0], 1: [0]}
for label, city_index in zip(labels, range(1, len(cities))):
    routes[label].append(cityindex)

# Ensuring both routes end at the depot
for key in routes:
    routes[key].append(0)

# Function for calculating the route cost
def calculate_route_cost(route):
    return sum(distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

# Function to perform the 2-opt swap
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if j - i == 1: continue  # Skip if cities are consecutive
                new_route = route[:i] + route[j:i - 1:-1] + route[j + 1:]
                if calculate_route_cost(new_route) < calculate_route_cost(best):
                    best = new_route
                    improved = True
        route = best
    return best

# Optimizing each route using 2-opt
optimized_routes = {0: two_opt(routes[0]), 1: two_opt(routes[1])}

# Output results
travel_costs = {}
for key in optimized_routes:
    cost = calculate_route_cost(optimized_routes[key])
    travel_costs[key] = cost
    print(f"Robot {key} Tour: {optimized_routes[key]}")
    print(f"Robot {key} Total Travel Cost: {cost}")

max_cost = max(travel_costs.values())
print(f"Maximum Travel `Cost: {max_cost}")