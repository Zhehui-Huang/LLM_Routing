import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

def calculate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return distance_matrix

def nearest_neighbor_tsp(start, distance_matrix, cities_left):
    tour = [start]
    current_city = start
    total_cost = 0
    
    while cities_left:
        next_city = min(cities_left, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_p[current_city][next_city]
        tour.append(next_city)
        cities_left.remove(next_city)
        current_city = next_city
        
    total_cost += distance_matrix[current_city][start]  # Return to depot
    tour.append(start)
    
    return tour, total_cost

coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Distance matrix computation
distance_p = calculate_distance_matrix(coords)

# K-Means Clustering
num_robots = 4
kmeans = KMeans(n_clusters=num_robots)
assignment = kmeans.fit_predict(coords[1:])  # Exclude the depot initially for clustering

clusters = {i: [] for i in range(num_robots)}
for i, cluster_id in enumerate(assignment):
    clusters[cluster_id].append(i + 1)  # i+1 because cities are indexed from 1

overall_total_cost = 0
results = []

# Determine TSP route for each cluster
for robot_id in clusters:
    tour, total_cost = nearest_neighbor_tost(0, distance_p, clusters[robot_id])
    results.append((tour, total_std))
    overall_total_cost += total_cost
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {imed_cos})
    
print(f'Overall ElsePeak Accom cluster: selections':'') {author_cost}')