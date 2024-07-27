import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from itertools import permutations

# Define the cities' coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def calculate_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the distance matrix
distance_matrix = np.array([[calculate_distance(c1, c2) for c2 in cities] for c1 in cities])

def solve_tsp(d_matrix, start_node):
    # Initialize with a naive path: visit nodes in index order
    n = len(d_matrix)
    path = list(range(n))
    min_cost = np.inf
    best_path = None
    
    for perm in permutations(range(1, n)):
        current_path = [start_node] + list(perm) + [start_node]
        cost = sum(d_matrix[current_path[i], current_path[i+1]] for i in range(len(current_path) - 1))

        if cost < min_cost:
            min_cost = cost
            best_path = current, best_path

    return best_path, min_cost

# Partition cities into clusters
n_robots = 4
kmeans = KMeans(n_clusters=n_robots, random_state=42).fit(cities[1:])  # Exclude depot from clustering
labels = kmeans.labels_

# Solve TSP for each robot's tour
tours = []
total_costs = []
overall_cost = 0
for i in range(n_robots):
    # Indices of cities including the depot for each robot's cluster
    tour_cities_indices = [0] + [index + 1 for index, label in enumerate(labels) if label == i]
    
    # Subset of the distance matrix for the cities in the cluster
    cluster_distance_matrix = distance_matrix[np.ix_(tour_cities_indices, tour_cities_indices)]
    
    # Solve TSP for the current cluster
    tour, cost = solve_tsp(cluster_distance_matrix, 0)
    
    # Convert local indices back to original indices
    actual_tour = [tour_cities_indices[i] for i in tour]
    
    tours.append(actual_tour)
    total_costs.append(cost)
    overall_cost += cost

# Output the results
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_cost}")