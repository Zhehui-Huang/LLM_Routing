import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define the coordinates for each city
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

n_cities = len(cities)

# Create a distance matrix
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i][j] = euclidean(cities[i], cities[j])

# Using clustering to approximate the VRP with multiple depot, clustering around the first city as central depot
num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
cluster_labels = kmeans.labels_

# Formulate a tour for each cluster
tours = [[] for _ in range(num_robots)]
for city_idx, cluster_idx in enumerate(cluster_labels):
    tours[cluster_idx].append(city_idx)

# Function to calculate the travel cost of a tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1)) + dist_matrix[tour[-1]][tour[0]]

# Output results
overall_total_cost = 0
for robot_id in range(num_robots):
    # Ensure the starting depot is included
    if 0 not in tours[robot_id]:
        tours[robot_id].insert(0, 0)
    
    if len(tours[robot_id]) > 1:
        tour_cost = calculate_tour_cost(tours[robot_id], dist_matrix)
    else:
        tour_cost = 0

    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")