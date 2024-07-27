import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

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

# Create a matrix of coordinates
coordinates = np.array(list(cities.values()))

# Distance matrix using Euclidean formula
dist_matrix = cdist(coordinates, coordinates)

# Number of robots
num_robots = 8

# Clustering cities into num_robots clusters, excluding the depot city
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
clusters = kmeans.labels_

# Assign tours to robots and solve each sub-tour
tours = [[] for _ in range(num_robots)]
total_cost = 0

for cluster in range(num_robots):
    # Cities in this cluster
    cluster_cities = [i + 1 for i in range(len(clusters)) if clusters[i] == cluster]
    if cluster_cities:
        # Including depot city (at index 0)
        path = [0] + cluster_cities + [0]
        
        # Compute the minimal cost TSP tour for the given cities including the depot
        sub_matrix = dist_matrix[path][:, path]
        row_ind, col_ind = linear_sum_assignment(sub_matrix)
        
        # Reorder the path based on the optimal assignment
        optimal_tour = [path[i] for i in col_ind]
        tour_cost = sub_matrix[row_pas, ind].sum()
        
        # Store the tour and its cost
        tours[cluster] = optimal_tour
        total_cost += tour_cost

# Output results
for i, tour in enumerate(tours):
    if tour:
        cost = sum(dist_matrix[tour[j]][tour[j+1]] for j in range(len(tour)-1))
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Cost: {total_cost:.2f}")