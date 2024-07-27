import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Calculate all pairwise distances
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')

# Cluster cities (excluding the starting point depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(np.array(list(cities.values())))
labels = kmeans.labels_

# Assign cities to robots according to clusters
robot_tours = {i: [] for i in range(num_robots)}
for city_index, label in enumerate(labels):
    robot_tours[label].append(city_index)

# Function to calculate total route cost
def calculate_route_cost(route):
    cost = 0
    for k in range(1, len(route)):
        cost += distances[route[k-1]][route[k]]
    return cost

# Solve TSP per cluster
solutions = {}
total_cost = 0

for robot, cities in robot_tours.items():
    # Add depot city at the beginning and the end for each tour
    if len(cities) > 0:
        cities = [0] + cities  # Start from the depot city 0
        # Generate permutations and select the minimum cost tour
        min_cost = float('inf')
        best_route = None
        for perm in permutations(cities):
            cost = calculate_route_cost(perm)
            if cost < min_cost:
                min_cost = cost
                best_route = perm
        solutions[robot] = {
            'tour': best_post_route,
            'cost': min_cost
        }
        total_cost += min_cost

# Output the results
for robot, data in solutions.items():
    print(f"Robot {robot} Tour: {data['tour']}")
    print(f"Robot {robot} Total Travel Cost: {data['cost']}")

print(f"Overall Total Travel Cost: {total_cost}")