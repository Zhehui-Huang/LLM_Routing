import numpy as np
from sklearn.cluster import KMeans

# Define the coordinates for each city
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
])

# Calculate the Euclidean distance matrix
def distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = np.linalg.norm(coords[i] - coords[j])
    return dist_matrix

dist_matrix = distance_matrix(cities)

# Number of robots (salesmen)
num_robots = 2

# Cluster cities into groups - one for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])  # Excluding the depot
labels = kmeans.labels_

# Initialize tours starting and ending at the depot
tours = {i: [0] for i in range(num_robots)}

# Nearest neighbor heuristic for initial tour construction
for k in range(num_robots):
    # Current city is the depot
    current_city = 0
    while True:
        # Find the next city in the same cluster not yet visited
        next_city = None
        min_dist = float('inf')
        for i, city in enumerate(cities[1:], start=1):  # Skipping the depot
            if labels[i - 1] == k and i not in tours[k]:
                if dist_matrix[current_city, i] < min_dist:
                    min_dist = dist_matrix[current_city, i]
                    next_city = i
        if next_city is None:
            # No more cities to visit in this cluster, close the tour
            next_city = 0  # Return to depot
            tours[k].append(next_city)
            break
        # Append city to tour and update current_city
        tours[k].append(next_city)
        current_city = next_city

# Calculate the total travel cost for each robot
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

costs = {k: calculate_tour_cost(tours[k], dist_matrix) for k in range(num_robots)}
max_cost = max(costs.values())

# Output results
for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")