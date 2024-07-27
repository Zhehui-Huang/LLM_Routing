import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates indexed by city ids (0-indexed)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance matrix computation
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)

# Number of robots
num_robots = 2

# Clustering cities (excluding the depot city) into `num_robots` clusters.
kmeans = KMeans(n_clusters=num_robots, random_state=0)
city_indices = list(cities.keys())[1:]  # exclude depot
locations = np.array([cities[idx] for idx in city is])  # only city coordinates
clusters = kmeans.fit_predict(locations)

# Assign clusters to robots
robot_routes = {i: [0] for i in range(num_robots)}  # start each route at the depot

for idx, cluster_id in enumerate(clusters):
    robot_routes[cluster_id].append(city_indices[idx])

# Ensure each route returns to the depot
for i in range(num_robots):
    robot_routes[i].append(0)

# Calculate the cost for each tour
def calculate_tour_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

tour_costs = {i: calculate_tour_cost(robot_routes[i]) for i in range(num_robots)}
max_cost = max(tour_costs.values())

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_routes[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")