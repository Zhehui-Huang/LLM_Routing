import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Determine the number of clusters/robots
num_clusters = 4

# Calculate distances between all pairs of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

dist_matrix = calculate_distances(cities)

# Clustering cities into groups for each depot using K-means
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(cities)
labels = kmeans.labels_

# Assign cities to each robot based on the K-means result
city_clusters = {i: [] for i in range(num_clusters)}
for i, label in enumerate(labels):
    city_clusters[label].append(i)

# Utilize Nearest Neighbor Strategy to determine tours within each cluster
def nearest_neighbor_tour(start, cities_subset, dist_matrix):
    tour = [start]
    current_city = start
    unvisited = set(cities_subset)
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start) # return to depot
    return tour

# Generate tours and calculate costs
tours = []
total_cost = 0
for robot in range(num_clusters):
    tour = nearest_neighbor_tour(robot, city_clusters[robot], dist_matrix)
    tours.append(tour)
    cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")