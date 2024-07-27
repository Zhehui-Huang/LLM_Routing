import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance_matrix

# City coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
])

# Number of robots, all starting from city 0
num_robots = 8
start_depot = 0

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# Calculate distance matrix
distance_mat = distance_matrix(cities, cities)

# Cluster cities using KMeans into equal groups for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(cities)
clusters = kmeans.labels_

# Helper function: find the shortest path through greedy nearest neighbor strategy for cities assigned to a robot
def find_shortest_path(indices, start_index):
    unvisited = set(indices)
    tour = [start_index]
    current_city = start_index

    while unvisited:
        unvisited.remove(current_city)
        if unvisited:  # still available cities to visit
            next_city = min(unvisited, key=lambda x: distance_mat[current_city][x])
            tour.append(next_city)
            current_city = next_city

    return tour

# Assigning cities to robots based on clusters
robots_tours = {i: [] for i in range(num_robots)}
for city_idx, cluster_idx in enumerate(clusters):
    robots_tours[cluster_idx].append(city_idx)

# Calculating the shortest tour for each robot
total_cost = 0.0
results = []

for robot_id, cities_indices in robots_tours.items():
    if cities_indices:
        tour = find_shortest_path(cities_indices, start_depot)
        tour_cost = sum(distance_mat[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += tour_cost

        results.append({
            'Robot ID': robot_id,
            'Tour': tour,
            'Tour Cost': tour_cost
        })

for result in results:
    print(f"Robot {result['Robot ID']} Tour: {result['Tour']}")
    print(f"Robot {result['Robot ID']} Total Travel Cost: {result['Tour Cost']:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")