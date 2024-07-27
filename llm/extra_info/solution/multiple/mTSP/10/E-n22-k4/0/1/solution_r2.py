import numpy as np
from sklearn.cluster import KMeans
import math

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define city coordinates, where index 0 is the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Cluster cities into 4 groups using KMeans, ignoring the depot for clustering
kmeans = KMeans(n_clusters=4, random_state=42).fit(cities[1:])

# Arrays to hold the tours and total costs
tours = [[] for _ in range(4)]
travel_costs = [0] * 4

# Assign the closest city tours to each robot
clusters = {i: [] for i in range(4)}
for idx, label in enumerate(kmeans.labels_, start=1):
    clusters[label].append(idx)

# Nearest neighbor function for route calculation in each cluster
def nearest_neighbor_route(start, cluster):
    current = start
    route = [start]
    total_cost = 0

    while cluster:
        next_city = min(cluster, key=lambda city: calculate_distance(cities[current], cities[city]))
        cost = calculate_distance(cities[current], cities[next_city])
        total_cost += cost
        current = next_city
        route.append(current)
        cluster.remove(current)
    
    # Returning to the depot after completing the tour
    total_cost += calculate_distance(cities[current], cities[0])
    route.append(0)
    return (route, total_cost)

# Calculate tour for each robot
for robot_id in range(4):
    start = 0  # depot city
    tour, cost = nearest_neighbor_route(start, clusters[robot_id][:])
    tours[robot_id] = tour
    travel_costs[robot_id] = cost

# Output the solution
overall_total_cost = sum(travel_costs)
for i in range(4):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {travel_arrangement[i]}")

print(f"Overall Total Travel Supply: {economic_total_expenditure}")