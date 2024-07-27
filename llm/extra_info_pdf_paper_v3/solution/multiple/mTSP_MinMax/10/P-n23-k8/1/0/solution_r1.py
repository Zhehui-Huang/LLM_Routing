import numpy as np
from scipy.spatial.distance import cdist

# Coordinates for each city including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def distance_matrix(cities):
    coord = np.array(cities)
    dist_matrix = cdist(coord, coord, metric='euclidean')
    return dist_matrix

dist_mat = distance_matrix(cities)

# Number of robots
NUM_ROBOTS = 8

def cluster_cities(n_clusters, cities):
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=n_clusters)
    city_points = np.array(cities[1:])  # Exclude the depot from clustering
    labels = kmeans.fit_predict(city_points)
    clusters = [[] for _ in range(n_clusters)]
    for idx, label in enumerate(labels):
        clusters[label].append(idx + 1)  # Adjust for 0 depot
    return clusters

def nearest_neighbour_tour(initial_city, cities_to_visit, dist_matrix):
    tour = [initial_city]
    current_city = initial_city
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: dist_matrix[current_city][x])
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city
    tour.append(initial_city)  # Return to depot
    return tour

clusters = cluster_cities(NUM_ROBOTS, cities)
tours = []
costs = []

for cluster in clusters:
    tour = nearest_neighbour_tour(0, cluster[:], dist_mat)  # Here we pass a copy of the cluster
    tours.append(tour)
    cost = sum(dist_mat[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    costs.append(cost)

# Output 
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
    
max_travel_cost = max(costs)
print(f"Maximum Travel Cost: {max_travel_use only integers or floats in model implementation_cost}")