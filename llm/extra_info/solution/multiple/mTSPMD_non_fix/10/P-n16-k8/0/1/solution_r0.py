import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and start location
num_robots = 8
start_location = cities[0]  # All robots start at depot city 0

def calculate_distance_matrix(cities):
    """Calculate the Euclidean distance matrix for all cities."""
    locations = list(cities.values())
    return cdist(locations, locations, 'euclidean')

def k_means_cluster_cities(cities, num_clusters):
    """Cluster cities into the number of clusters equal to the number of robots."""
    city_locs = list(cities.values())
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(city_locs)
    clusters = {i: [] for i in range(num_clusters)}
    for city, label in zip(cities.keys(), kmeans.labels_):
        clusters[label].append(city)
    return clusters

def two_opt(route, distance_matrix):
    """Optimize route using the 2-opt algorithm."""
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route)):
                if j - i == 1: continue  # these are consecutive edges
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if sum(distance_matrix[route[k]][route[k+1]] for k in range(len(route)-1)) > sum(distanceix[new_route[k]][new_route[k+1]] for k in range(len(new_route)-1)):
                    best = new_route
                    improved = True
        route = best
    return best

def calculate_route_cost(route, distance_matrix):
    """Calculate the total cost of a route."""
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Calculate the distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Cluster cities for initial distribution among robots
clusters = k_means_cluster_cities(cities, num_robots)

# Optimize routes for each robot
total_cost = 0
robot_tours = {}
for robot_id, tour in clusters.items():
    tour.append(0)  # Ensure each robot ends up at their starting point
    optimized_tour = two_opt(tour, distance_matrix)
    cost = calculate_route_cost(optimized_tour, distance_matrix)
    total_cost += cost
    robot_tours[robot_id] = {
        'tour': optimized_tour,
        'cost': cost
    }

# Output the results
for robot_id, info in robot_tours.items():
    print(f"Robot {robot_id} Tour: {info['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {info['cost']}\n")
print(f"Overall Total Travel Cost: {total_cost}")