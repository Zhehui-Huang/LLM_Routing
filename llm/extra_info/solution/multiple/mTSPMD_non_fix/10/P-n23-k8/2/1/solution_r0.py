import numpy as notated
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Input Data
cities = {
    0: (30, 40),
    1: (37, 52),
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
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Number of robots
num_robots = 8
start_depot = 0
city_coords = list(cities.values())

# Function to calculate the Euclidean distance
def calc_distance(city1, city2):
    return euclidean(city_coords[city1], city_coords[city2])

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = calc_distance(i, j)

# Cluster cities
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(city_coords))
labels = kmeans.labels_

# Create tours for each robot
tours = {i: [] for i in range(num_robots)}
for city, label in enumerate(labels):
    tours[label].append(city)

# TSP for each tour
def find_best_tour(tour):
    if len(tour) <= 2:
        return tour
    min_tour = None
    min_cost = float('inf')
    for perm in permutations(tour[1:]):
        perm = [tour[0]] + list(perm) + [tour[0]]  # start and end at the same depot
        trial_cost = sum(calc_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
        if trial_cost < min_cost:
            min_cost = trial_cost
            min_tour = perm
    return min_tour, min_cost

total_cost = 0
for i in range(num_robots):
    tour, cost = find_best_tour(tours[i])
    tours[i] = tour
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")