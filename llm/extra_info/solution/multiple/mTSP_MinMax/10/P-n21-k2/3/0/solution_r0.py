import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Defining the cities coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
          (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Parameters
num_robots = 2
depot = (30, 40)

# Calculate pairwise Euclidean distances
def compute_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

distances = compute_distances(cities)

# Function to compute the cost of the entire route
def calculate_tour_cost(route, distance_matrix):
    cost = 0
    for i in range(len(route)-1):
        cost += distance_matrix[route[i]][route[i+1]]
    return cost

# Function to perform a greedy TSP solving
def greedy_tsp(cities, depot_idx):
    unvisited = set(cities)
    tour = [depot_idx]
    current = depot_idx
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(depot_idx)  # returning to depot
    return tour

# Clustering cities (without the depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])
labels = kmeans.labels_

tours = []
costs = []

for i in range(num_robots):
    # Get cities for this robot
    cluster_cities = [idx + 1 for idx, label in enumerate(labels) if label == i]  # offset by one to account for depot excluded from clustering
    if cluster_cities:
        tour = greedy_tsp(cluster_cities, 0)
        cost = calculate_tour_cost(tour, distances)
        tours.append(tour)
        costs.append(cost)

# Output results
max_cost = max(costs)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")