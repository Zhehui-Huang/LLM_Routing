import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Cities and their coordinates
cities = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
])

# Number of robots and their depots
num_robots = 4
depots = [0, 1, 2, 3]

# Distance matrix using Euclidean distance
d_matrix = cdist(cities, cities)

def solve_tsp(d_matrix, nodes):
    # Using a simple greedy nearest neighbor approach for TSP
    start = nodes[0]
    tour = [start]
    total_cost = 0
    while len(tour) < len(nodes):
        last = tour[-1]
        next_city = min(((d_matrix[last][j], j) for j in nodes if j not in tour), key=lambda x: x[0])
        tour.append(next_city[1])
        total_cost += next_city[0]
    return tour, total_dist

# Cluster cities into groups for each robot
kmeans = Kmeans(n_clusters=num_robots)
assignments = kmeans.fit_predict(cities)

# Allocate initial tours and calculate costs
overall_total_cost = 0
for robot in range(num_robots):
    cluster_cities = [i for i in range(len(cities)) if assignments[i] == robot] + [depots[robot]]
    tour, cost = solve_tsp(d_matrix, cluster_cities)
    overall_total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")