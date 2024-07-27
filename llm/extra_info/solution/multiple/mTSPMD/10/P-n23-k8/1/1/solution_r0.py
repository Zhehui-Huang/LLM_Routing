import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Coordinates of each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their respective depots
num_robots = 8
depots = list(range(num_robots))

# Distance matrix calculation
def compute_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = compute_distance_matrix(coordinates)

# Assigning cities to robots using KMeans clustering
kmeans = KMeans(n_clusters=num_robots, init=np.array([coordinates[d] for d in depots]), n_init=1)
labels = kmeans.fit_predict(coordinates)

# Nearest Neighbor Algorithm for TSP
def nearest_neighbor_tour(start, cities_to_visit, dist_matrix):
    tour = [start]
    current = start
    total_cost = 0.0
    
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: dist_matrix[current, x])
        total_cost += dist_matrix[current, next_city]
        current = next_city
        tour.append(current)
        cities_to_visit.remove(current)
        
    # return to the starting depot
    total_cost += dist_matrix[current, start]
    tour.append(start)
    return tour, total_cost

# Compute the tours for each robot
tours = []
costs = []
overall_cost = 0

for robot in range(num_robots):
    assigned_cities = [i for i, d in enumerate(labels) if d == robot and i not in depots]
    tour, cost = nearest_neighbor_tour(depots[robot], assigned_cities, dist_matrix)
    tours.append(tour)
    costs.append(cost)
    overall_cost += cost

    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")