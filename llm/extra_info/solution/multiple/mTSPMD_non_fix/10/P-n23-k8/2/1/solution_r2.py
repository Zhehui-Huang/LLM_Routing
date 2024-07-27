import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Starting points for all robots (assumption: they start from the same depot city 0)
start_depot = 0

# Calculate Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# Create a matrix of distances
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = calculate_distance(i, j)

# K-means to cluster cities for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(list(cities.values())))
labels = kmeans.labels_

# Assign each city to a robot's tour
tours = {i: [] for i in range(num_robots)}
for city_index, label in enumerate(labels):
    tours[label].append(city_index)

# Function to find the minimum cost tour using permutations brute force (feasible for small set of cities per robot)
def find_min_cost_tour(tour):
    smallest_cost = float('inf')
    best_tour = None
    for perm in permutations(tour):
        # Ensuring the tour starts at the depot for each robot
        if perm[0] != start_depot:
            continue
        cost = sum(distance_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
        if cost < smallest_cost:
            smallest_cost = cost
            best_tour = perm
    return best_tour, smallest_cost

# Calculate optimized tours and the costs
total_cost = 0
for robot_id in tours:
    tour, cost = find_min_cost_tour(tours[robot_id] + [start_deposit])  # Ensure returning to start depot
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")