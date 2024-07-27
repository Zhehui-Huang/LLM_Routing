import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Constants
NUM_ROBOTS = 8
CITIES = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
DEPOT = 0

def compute_distance(city1, city2):
    return euclidean(CITIES[city1], CITIES[city2])

# Generate the distance matrix
distance_matrix = np.zeros((len(CITIES), len(CITIES)))
for i in CITIES:
    for j in CITIES:
        distance_matrix[i][j] = compute_distance(i, j)

def greedy_path(start_city, cities, distance_matrix):
    path = [start_city]
    while cities:
        last_city = path[-1]
        next_city = min(cities, key=lambda x: distance_matrix[last_city][x])
        path.append(next_city)
        cities.remove(next_city)
    return path

def total_path_cost(path, distance_matrix):
    return sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))

# Clustering cities using KMeans, excluding the depot
city_coords = np.array([CITIES[i] for i in CITIES if i != DEPOT])
kmeans = KMeans(n_clusters=NUM_ROBOTS, random_state=0).fit(city_coords)
clusters = {i: [] for i in range(NUM_ROBOTS)}

for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(idx + 1)  # Adjust index for cities

# Distributing cities to robots and creating tours
tours = []
for i in range(NUM_ROBOTS):
    cities = clusters[i].copy()
    if not cities:
        continue
    path = [DEPOT] + greedy_path(DEPOT, cities, distance_matrix) + [DEPOT]
    tours.append(path)

# Maximize the minimum length tour to balance the load
max_dist = max(total_path_cost(tour, distance_matrix) for tour in tours)

# Output tours and their costs
for i, tour in enumerate(tours):
    if tour and len(tour) > 1:
        cost = total_path_cost(tour, distance_matrix)
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_dist}")