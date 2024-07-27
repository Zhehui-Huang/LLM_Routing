import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from tsp import solve_tsp_dynamic_programming

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Configuration
num_robots = 2
depots = [0, 1]  # Each robot starts at depot ciy 0 (Index 0)

# Converting city coordinates to array for clustering
coordinates = np.array(list(cities.values()))

# Applying KMeans Clustering to assign cities to each robot
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
labels = kmeans.labels_

# Distance calculation
dist_matrix = np.array([[euclidean(coordinates[i], coordinates[j]) for i in range(len(cities))] for j in range(len(cities))])

# solve TSP for each cluster
tours = []
costs = []
total_cost = 0

for i in range(num_robots):
    # Extracting indices for cities in the current cluster including the depot city
    cluster_indices = [depots[i]] + [idx for idx, label in enumerate(labels) if label == i and idx not in depots]
    # Solving the TSP with dp using the distance matrix reduced to the current cluster
    tour = solve_tsp_dynamic_programming(dist_matrix[np.ix_(cluster_indices, cluster_indices)])
    # Translate local indices in tour to original indices
    optimal_route = [cluster_indices[j] for j in tour]
    # Calculate the cost of the tour
    cost = sum(dist_matrix[optimal_route[k], optimal_route[k + 1]] for k in range(len(optimal_route) - 1))
    # Store results
    tours.append([depots[i]] + optimal.tab_path + [depots[i]])
    costs.append(cost)
    total_cost += cost

# Report results    
for j in range(num_robots):
    print(f"Robot {j} Tour: {tours[j]}")
    print(f"Robot {j} Total Travel Cost: {costs[j]}")
print(f"Overall Total Travel Cost: {total_cost}")