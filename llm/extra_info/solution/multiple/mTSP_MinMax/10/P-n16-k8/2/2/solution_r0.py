import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Given city coordinates (Depot is index 0)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots (clusters)
num_robots = 8

# Prepare the data for clustering (excluding the depot city)
data = np.array([coord for id, coord in cities.items() if id != 0])

# K-means clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(data)
labels = kmeans.labels_

clusters = {i: [] for i in range(num_robots)}
for city_index, label in enumerate(labels, 1):
    clusters[label].append(city_index)

# Calculate the distance matrix
def calc_distance_matrix(points):
    num_points = len(points)
    distance_matrix = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                distance_matrix[i][j] = euclidean(points[i], points[j])
            else:
                distance_matrix[i][j] = 0
    return distance_matrix

# Traveling Salesman Problem solver using a simple 2-opt approach
def tsp_2opt(cities, dist_matrix):
    n = len(cities)
    tour = list(range(n))
    improved = True

    while improved:
        improved = False
        for i in range(1, n-2):
            for j in range(i+2, n):
                if j - i == 1: continue
                old_cost = dist_matrix[tour[i-1]][tour[i]] + dist_matrix[tour[j]][tour[j+1]]
                new_cost = dist_matrix[tour[i-1]][tour[j]] + dist_matrix[tour[i]][tour[j+1]]
                if new_cost < old_cost:
                    tour[i:j] = reversed(tour[i:j])
                    improved = True

    integrated_tour = [0] + [cities[t] for t in tour] + [0]
    return integrated_tour

# Assign tours to robots and calculate the costs
robot_tours = []
max_cost = 0

for robot, cities in clusters.items():
    if cities:
        cluster_cities = [0] + cities
        
        # Calculate distance matrix for current cluster including the depot
        dist_matrix = calc_distance_matrix([cities[coord] for coord in cluster_cities])
        
        # Run TSP solver
        tour = tsp_2opt(cluster_cities, dist_matrix)
        
        # Calculate cost for this tour
        cost = sum(euclidean(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        robot_tours.append((tour, cost))
        max_cost = max(max_cost, cost)

# Printing the results
for idx, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")