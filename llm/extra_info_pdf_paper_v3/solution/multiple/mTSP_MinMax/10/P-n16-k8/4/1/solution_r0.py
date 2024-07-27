import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates as specified
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
          (43, 67), (58, 48), (58, 27), (37, 69)]

# Function to calculate distances between cities
def calc_distance(city1, city2):
    return euclidean(city1, city2)

# Generate matrix of distances
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calc_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# K-means Clustering to assign initial groups (robots) to cities
kmeans = KMeans(n_clusters=8, random_state=0)
clusters = kmeans.fit_predict(cities[1:])
cluster_mapping = {i + 1: cluster for i, cluster in enumerate(clusters)}

# Assign clusters to robots
robot_tours = {i: [0] for i in range(8)}  # start each tour from depot city 0
for city, cluster in cluster_mapping.items():
    robot_tours[cluster].append(city)

# Add depot city at the end of each path to return
for tour in robot_tours.values():
    tour.append(0)

# Calculate travel cost for a given tour
def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Calculate tour costs 
tour_costs = {}
max_cost = 0
for i, tour in robot_tours.items():
    cost = calculate_cost(tour)
    tour_costs[i] = cost
    max_cost = max(max_cost, cost)

# Output the tours and costs
for i, tour in robot_tours.items():
    print(f"Robot {i} Tour:", tour)
    print(f"Robot {i} Total Travel Cost:", tour_costs[i])
print("Maximum Travel Cost:", max_cost)