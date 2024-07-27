import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import itertools

# Define the cities' coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate the distance matrix
dist_matrix = cdist(cities, cities, metric='euclidean')

# Partition cities into clusters
n_robots = 4
kmeans = KMeans(n_clusters=n_robots, random_state=42).fit(cities[1:])  # Exclude depot from clustering
labels = kmeans.labels_

def tsp_solver(sub_dist_matrix):
    # Start at the first city, iterate over permutations of the others
    nodes = list(range(len(sub_dist_matrix)))
    shortest_route = None
    min_cost = float('inf')
    
    for route in itertools.permutations(nodes[1:]):
        route = [nodes[0]] + list(route) + [nodes[0]]
        cost = sum(sub_dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        
        if cost < min_cost:
            min_cost = cost
            shortest_route = route
            
    return shortest_route, min_cost

overall_cost = 0
solution = []

for i in range(n_robots):
    cluster_indices = [0] + [index + 1 for index, label in enumerate(labels) if label == i]
    cluster_dist_matrix = dist_matrix[np.ix_(cluster_indices, cluster_indices)]
    
    tour, cost = tsp_solver(cluster_dist_matrix)
    mapped_tour = [cluster_indices[x] for x in tour]
    
    overall_cost += cost
    solution.append((mapped_tour, cost))

# Output the results
for robot_id, (tour, cost) in enumerate(solution):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")