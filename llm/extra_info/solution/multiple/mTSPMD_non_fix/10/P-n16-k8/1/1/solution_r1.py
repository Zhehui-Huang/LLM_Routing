import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculating Euclidean distance matrix manually
def calculate_distance_matrix(locations):
    n = len(locations)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i, j] = euclidean(locations[i], locations[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Solving the TSP using a very basic nearest neighbor algorithm
def tsp_nearest_neighbor(dist_matrix, start_point):
    n = len(dist_matrix)
    visit_mask = np.zeros(n, dtype=bool)
    tour = [start_point]
    visit_mask[start_point] = True

    current_point = start_point
    while len(tour) < n:
        next_point = np.argmin(np.where(visit_mask, np.inf, dist_matrix[current_point]))
        visit_mask[next_point] = True
        tour.append(next_point)
        current_point = next_point

    return tour

# Clustering cities into 8 groups
num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
labels = kmeans.labels_

# Assigning cities to each robot and solving the TSP
tours = []
for i in range(num_robots):
    cities_indices = np.where(labels == i)[0]
    if len(cities_indices) > 1:
        starting_point = cities_indices[0]  # Just pick the first city in cluster for simplification
        tour = tsp_nearest_neighbor(distance_matrix[np.ix_(cities_indices, cities_indices)], 0)
        real_tour = cities_indices[tour].tolist()
    else:
        real_tour = cities_indices.tolist()
    tours.append(real_tour)

# Calculate the total and individual costs
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = 0
    for j in range(len(tour) - 1):
        tour_cost += distance_matrix[tour[j], tour[j + 1]]
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Total Cost: {tour_cost:.2f}")

print(f"Overall Total Cost: {total_cost:.2f}")