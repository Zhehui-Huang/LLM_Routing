import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# City coordinates including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# The function to calculate Euclidean distance
def calc_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Heuristic: Nearest Neighbour to find shortest path
def nearest_neighbour_tour(start_index, cities, coords):
    tour = [start_index]
    current_index = start_index
    total_cost = 0
    while len(tour) < len(cities) + 1:
        nearest = None
        min_distance = float('inf')
        for i in cities:
            if i not in tour:
                dist = calc_distance(coords[current_index], coords[i])
                if dist < min_distance:
                    min_distance = dist
                    nearest = i
        total_cost += min_distance
        current_index = nearest
        tour.append(nearest)
    # Connect back to the start
    total_cost += calc_distance(coords[tour[-1]], coords[start_index])
    tour.append(start_index)
    return tour, total_cost

# Depots start indexing
depot_starts = [0]

coords_array = np.array(coordinates)
kmeans = KMeans(n_clusters=4, random_state=0).fit(coords_array)
clusters = kmeans.labels_

overall_cost = 0
results = []

for i in range(4):
    cities_in_cluster = np.where(clusters == i)[0]
    tour, cost = nearest_neighbour_tour(depot_starts[0], cities_in_cluster, coordinates)
    results.append((i, tour, cost))
    overall_cost += cost

# Output formatting
for robot_id, tour, cost in results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Summer Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")