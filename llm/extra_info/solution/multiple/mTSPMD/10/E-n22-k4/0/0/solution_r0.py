import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from itertools import permutations

# List of city coordinates
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), 
               (128, 252), (163, 247), (146, 246), (161, 242), 
               (142, 239), (163, 236), (148, 232), (128, 231), 
               (156, 217), (129, 214), (146, 208), (164, 208), 
               (141, 206), (147, 193), (164, 193), (129, 189), 
               (155, 185), (139, 182)]

n_cities = len(coordinates)

# Compute Euclidean distance matrix
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Cluster cities into 4 clusters (for 4 robots)
kmeans = KMeans(n_clusters=4, random_state=0).fit(coordinates[4:])
labels = kmeans.labels_

# Append depot cities to respective clusters
clusters = {i: [i] for i in range(4)}  # Start each cluster with its depot city
for idx, label in enumerate(labels, 4):
    clusters[label].append(idx)

# Function to find minimum cost tour using permutations
def find_min_tour(cities):
    min_path = None
    min_cost = float('inf')
    for perm in permutations(cities):
        cost = sum(dist_matrix[perm[i]][perm[i+1]] for i in range(len(perm) - 1))
        cost += dist_matrix[perm[-1]][perm[0]]  # returning to start
        if cost < min_cost:
            min_cost = cost
            min_path = perm
    return min_path, min_cost

# Solve TSP for each robot using their respective city cluster
tours = {}
total_cost = 0
for robot in range(4):
    tour, cost = find_min_tour(clusters[robot])
    tours[robot] = tour + (tour[0],)  # Complete the loop back to depot
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel ICost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total不cost}")