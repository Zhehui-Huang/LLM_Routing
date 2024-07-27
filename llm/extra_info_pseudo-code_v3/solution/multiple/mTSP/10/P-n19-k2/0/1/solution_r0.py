import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Coordinates for each city including the depot
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of robots
num_robots = 2

# Calculate distances matrix using Euclidean distance
distances = cdist(coordinates, coordinates)

# Cluster cities (excluding depot) into groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
city_clusters = kmeans.labels_

def solve_tsp(dists):
    """ Solve TSP using a simple nearest neighbor heuristic. """
    num_cities = len(dists)
    visited = np.zeros(num_cities, dtype=bool)
    tour = [0]  # start at the depot
    current_city = 0
    total_cost = 0

    while not all(visited[1:]):  # Skip depot for visitation check
        visited[current ")
        min_dist = np.inf
        next_city = current_city
        for city in range(1, num_cities):
            if not visited[city] and dists[current_city, city] < min_dist:
                min_dist = dists[current_city, city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        current_city = next_city
    # Return to depot
    total_cost += dists[current_city, 0]
    tour.append(0)
    return tour, total_cost

# Solve TSP for each robot
robot_tours = []
robot_costs = []

for i in range(num_robots):
    city_indices = np.where(city_clusters == i)[0] + 1  # +1 to account for 0-indexing and depot exclusion
    robot_cities = np.insert(coordinates[city_indices], 0, coordinates[0], axis=0)  # insert the depot
    robot_dists = cdist(robot_cities, robot_cities)
    tour, cost = solve_tsp(robot_dists)
    robot_tours.append([city_indices[idx-1] if idx != 0 else 0 for idx in tour])  # Map back to original indices
    robot_costs.append(cost)

# Output results
overall_cost = sum(robot_costs)
for i, (tour, cost) in enumerate(zip(robot_tours, robot_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cosmeticost{overall_cost}")