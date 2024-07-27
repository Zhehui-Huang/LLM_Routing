import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Calculate Euclidean Distance Matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return distance_matrix

# Nearest Neighbor Algorithm for TSP
def nearest_neighbor_tsp(start, distance_matrix, cities_left):
    tour = [start]
    current_city = start
    total_cost = 0
    
    while cities_left:
        next_city = min(cities_left, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        cities_left.remove(next_city)
        current_city = next_city
        
    total_cost += distance_matrix[current_city][start]  # Return to start
    tour.append(start)
    
    return tour, total_cost

coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Creating distance matrix 
distance_matrix = calculate_distance_matrix(coords)

# Clustering cities for each robot using KMeans
kmeans = KMeans(n_clusters=4)
assignments = kmeans.fit_predict(np.array(coords[1:]))  # Exclude the depot for clustering purposes

clusters = {i: [] for i in range(4)}
for idx, cluster_id in enumerate(assignments):
    clusters[cluster_id].append(idx+1)  # city indices start from 1

overall_total_cost = 0

# Solving TSP for each cluster starting from the depot, which is city 0
for robot_id in clusters:
    cities = [0] + clusters[robot_id]  # Adding depot to the cities list
    tour, total_cost = nearest_neighbor_tsp(0, distance_matrix, cities)
    overall_total_cost += total_cost
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {total_cost}')

print(f'Overall Total Travel Cost: {overall_total_cost}')