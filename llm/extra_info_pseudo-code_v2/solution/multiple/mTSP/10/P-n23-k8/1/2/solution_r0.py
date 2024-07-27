import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Define the coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Compute distance matrix
def euclidean_distance_matrix(coords):
    return cdist(coords, coords)

distance_matrix = euclidean_distance_matrix(coordinates)

# Function to cluster cities for initial distribution among robots
def cluster_cities(coordinates, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coordinates)
    cluster_labels = kmeans.labels_
    return cluster_labels

# Assign initial cities to the robots using clustering
city_indices = np.arange(1, len(coordinates))  # Exclude the depot (index 0)
cluster_labels = cluster_cities(np.array(coordinates)[city_indices], num_robots)
robots_cities = {i: [] for i in range(num_robots)}
for idx, label in zip(city_indices, cluster_labels):
    robots_cities[label].append(idx)

# Utility function to compute the total travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return cost

# Improve individual tour using 2-opt
def two_opt(tour, distance_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour, distance_matrix) < calculate_tour_cost(best, distance_matrix):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Construct initial tours and optimize
robot_tours = {}
overall_total_cost = 0
for robot_id, cities in robots_cities.items():
    tour = [0] + cities + [0]
    optimized_tour = two_opt(tour, distance_matrix)
    tour_cost = calculate_tour_cost(optimized_tour, distance_matrix)
    robot_tours[robot_id] = {'tour': optimized_tour, 'cost': tour_cost}
    overall_total_cost += tour_cost

# Print the results
for robot_id, data in robot_tours.items():
    print(f"Robot {robot_id} Tour: {data['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {data['cost']}")
print(f"Overall Total Travel Cost: {overall_total_cost}")