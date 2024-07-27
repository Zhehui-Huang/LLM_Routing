import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from pytsp import atsp_tsp, run_concorde

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate distance matrix
n_cities = len(coordinates)
dist_matrix = np.zeros((n_cities, n_cities), dtype=float)
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Number of robots
num_robots = 2

# K-means clustering to distribute cities (excluding the depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # Without depot
labels = kmeans.labels_

# Determine tours and costs
tours = [[] for _ in range(num_robots)]
total_costs = [0] * num_robots

for robot in range(num_robots):
    cluster_indices = [i + 1 for i, label in enumerate(labels) if label == robot]  # +1 to consider depot shift
    cluster_indices = [0] + cluster_indices + [0]  # Add the depot city at the start and end
    dist_subset = dist_matrix[np.ix_(cluster_indices, cluster_index)]
    
    # Get TSP solution for each robot's city subset
    matrix_sym = atsp_tsp(dist_subset, strategy="avg")
    tour_data = run_concorde(matrix_sym, solver="concorde", verbose=False)
    robot_tour = [cluster_indices[i] for i in tour_data['tour']]
    robot_cost = tour_data['tour_cost']
    
    tours[robot] = robot_tour
    total_costs[robot] = robot_cost

# Outputting the results
overall_cost = sum(total_costs)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall(memory_costh_cost}\n")

### End of code