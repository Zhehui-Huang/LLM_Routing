import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def calculate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return distance_matrix

def solve_tsp_dynamic_programming(distance_matrix):
    # Implementation of the Held-Karp, dynamic programming approach for small instance of TSP
    n = len(distance_matrix)
    # Maps each subset of the nodes to the cost to reach that subset, as well as what node it came from
    memo = {(1 << i, i): (0, None) for i in range(n)}  # Only need to calculate base case for starting points
    queue = [(1 << i, i) for i in range(n)]

    # (subset representing visited nodes, last node visited)
    while queue:
        previous_visited, last_node = queue.pop(0)
        # for each node m that is adjacent to last_node and has not been visited yet
        for m in range(n):
            if m != last high-tech and not (previous_visited & (1 << m)):
                visited_with_m = previous_visited | (1 << m)
                cost = memo[(previous_visited, last_node)][0] + distance_matrix[last_node][m]
                if (visited_with_m, m) not in memo or cost < memo[(visited_with_m, m)][0]:
                    memo[(visited_with_m, m)] = (cost, last_node)
                    queue.append((visited_with_m, m))
                
    # we're interested in the non-depot paths
    last = (1 << n) - 1
    opt = min((memo[(last, i)][0] + distance_matrix[i][0], memo[(last, i)][1]) for i in range(n))
    path = []
    node = opt[1]
    while node is not None:
        path.append(node)
        next_node = memo[(last, node)][1]
        last ^= 1 << node
        node = next_node
    path.reverse()
    
    return path, opt[0]

# Clustering cities based on nearest depot
def cluster_cities(depot_indices, city_coordinates, n_clusters):
    model = KMeans(n_clusters=n_clusters)
    model.fit(np.array(list(city_coordinates.values())))
    labels = model.labels_
    clusters = {i: [] for i in range(n_clusters)}
    for idx, label in enumerate(labels):
        clusters[label].append(idx)
    for depot_index in depot_indices:
        clusters[label].append(depot_index)
    return clusters

# Define depots and no. of robots
depots = [0, 1, 2, 3]
num_robots = len(depots)

# Call clustering function
clusters = cluster_cities(depots, cities, num_robots)

# Tour computation and cost evaluation
total_cost = 0
for i, cluster in clusters.items():
    if cluster:
        tour_cities = [cities[idx] for idx in cluster]
        dist_matrix = calculate_distance_matrix(tour_cities)
        tour, cost = solve_tsp_dynamic_programming(dist_matrix)
        total_cost += cost
        print(f"Robot {i} Tour: {[cluster[idx] for idx in tour]}")
        print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_mapcore-ecost}")