import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the cities coordinates (excluding the depot)
cities = [
    (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 48), (58, 27), (37, 69)
]
depot = (30, 40)
cities.insert(0, depot)  # insert depot at index 0

# Number of robots
num_robots = 8

# Clustering the cities into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=42)
clusters = kmeans.fit_predict(cities)
clustered_cities = {i: [] for i in range(num_robots)}

for city_index, cluster_id in enumerate(clusters):
    clustered_cities[cluster_id].append(city_index)

# Function to compute the total distance of a given tour
def compute_tour_distance(tour, city_coordinates):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return distance

# Solving TSP for each robot using a simple nearest neighbor heuristic for now (This can be optimized further)
def solve_tsp(cities):
    if len(cities) <= 2:
        return cities + [cities[0]]
    permutations_of_cities = list(permutations(cities))
    min_distance = float('inf')
    best_tour = None
    for perm in permutations_of_cities:
        # consider a cycle back to the start post permutations
        tour = list(perm) + [perm[0]]
        distance = compute_tour_distance(tour, cities)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    return best_tour

# Calculate tours and distances for each robot
overall_total_distance = 0

for i in range(num_robots):
    tour = solve_tsp(clustered_cities[i])
    tour_distance = compute_tour_distance(tour, cities)
    overall_total_distance += tour_distance
    print(f'Robot {i} Tour: {tour}')
    print(f'Robot {i} Total Travel Cost: {tour_distance:.2f}')

print(f'Overall Total Travel Cost: {overall_total_distance:.2f}')