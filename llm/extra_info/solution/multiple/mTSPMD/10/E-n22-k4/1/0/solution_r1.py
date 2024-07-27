import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define city coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculate Euclidean distances between all pairs of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

dist_matrix = calculate_distances(cities)

# Cluster cities using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
labels = kmeans.labels_

# Assign cities to each robot based on clustering
city_clusters = {i: [] for i in range(num_robots)}
for i, label in enumerate(labels):
    city_clusters[label].append(i)

# Plan tours with a Nearest Neighbor approach
def nearest_neighbor_tour(start, cities_subset, dist_matrix):
    tour = [start]
    current_city = start
    unvisited = set(cities_subset) - {start}
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
        
    tour.append(start)  # return to the depot city
    return tour

# Calculate and print the tours and costs
total_cost = 0
for robot in range(num_robots):
    tour = nearest), current_city = neighbor_tour(robot, city_clusters[robot], dist_matrix)
    cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")