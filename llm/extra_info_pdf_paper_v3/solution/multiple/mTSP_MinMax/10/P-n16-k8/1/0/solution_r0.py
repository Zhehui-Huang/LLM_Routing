import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

def calculate_distance(city1, city2):
    return euclidean(city1, city2)

def create_initial_clusters(num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    positions = np.array(cities[1:])  # Exclude depot
    kmeans.fit(positions)
    clusters = {i: [] for i in range(num_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(idx + 1)  # +1 to correct index since depot is excluded
    return clusters

def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if calc_route_cost(new_route) < calc_route_cost(best):
                    best = new_route
                    improved = True
    return best

def calc_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += calculate_distance(cities[route[i]], cities[route[i + 1]])
    return total_cost

# Assign initial clusters
clusters = create_initial_clusters(num_robots)

# Perform individual optimization using 2-opt for each cluster
tours = {}
max_travel_cost = 0

for robot_id, city_indices in clusters.items():
    tour = [0] + city_indices + [0]
    optimized_tour = two_opt(tour)
    tour_cost = calc_route_cost(optimized_tour)
    tours[robot_id] = (optimized_tour, tour_cost)
    max_travel_cost = max(max_travel_cost, tour_cost)

# Output the results
for robot_id, (tour, cost) in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")