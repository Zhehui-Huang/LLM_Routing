import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance_matrix
from tsp_solver.greedy import solve_tsp_dynamic_programming

# Define the cities and their coordinates
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

# Calculate distances between each pair of cities
coordinates = np.array(list(cities.values()))
dist_matrix = distance_matrix(coordinates, coordinates)

# Number of robots
num_robots = 8

# Clustering cities into num_robots clusters
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot
clusters = kmeans.labels_

# Organize cities by clusters and solve TSP for each cluster
tours = []
total_cost = 0

for r in range(num_robots):
    # Get the cities indices in this cluster
    cluster_indices = [i+1 for i, c in enumerate(clusters) if c == r]  # offset by 1 to account for city indices starting at 1
    if cluster_indices:
        # TSP solution for the current cluster including a return to the depot
        full_path = [0] + cluster_indices + [0]  # start and end at the depot
        sub_matrix = dist_matrix[full_path][:, full_path]
        tour_indices = solve_tsp_dynamic_programming(sub_matrix)
        tour = [full_path[i] for i in tour_indices]
        tour_cost = sum(sub_matrix[tour_indices[i], tour_indices[i+1]] for i in range(len(tour_indices)-1))
        
        # Store and report the tour and its total cost
        tours.append((tour, tour_cost))
        total_cost += tour_cost

# Output each robot's tour and the respective costs
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Comst: {total_cost:.2f}")