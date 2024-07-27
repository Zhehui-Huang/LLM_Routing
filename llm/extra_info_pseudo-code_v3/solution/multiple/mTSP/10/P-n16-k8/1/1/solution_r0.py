import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# City coordinates, excludes the depot city as a destination
cities = [(37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
          (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
depot = (30, 40)

# Number of robots available
num_robots = 8

# Euclidean distance function
def calculate_distance(city1, city2):
    return euclidean(city1, city2)

# Initialize K-means
kmeans = KMeans(n_clusters=num_robots, random_state=0)
assignments = kmeans.fit_predict(cities)

# 2-opt optimization function
def two_opt(route, dist_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i+1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if dist_matrix[new_route].sum() < dist_matrix[best].sum():
                    best = new_route
                    improved = True
        route = best
    return best

# Distance matrix initialization for each robot based on city cluster
overall_total_cost = 0

for robot_id in range(num_robots):
    cluster_cities = [depot] + [cities[i] for i in range(len(cities)) if assignments[i] == robot_id]
    dist_matrix = np.zeros((len(cluster_cities), len(cluster_cities)))
    
    for i, city1 in enumerate(cluster_cities):
        for j, city2 in enumerate(cluster_cities):
            dist_matrix[i, j] = calculate_distance(city1, city2)
            
    # Initial route (naive sequence)
    initial_route = list(range(len(cluster_cities)))
    
    # Optimize tour using 2-opt
    optimized_route_indices = two_opt(initial_route, dist_matrix)
    optimized_route = [cluster_cities[i] for i in optimized_route_indices] + [depot]  # return to depot
    
    # Calculate individual travel cost
    individual_cost = sum(calculate_distance(optimized_route[i], optimized_route[i+1]) for i in range(len(optimized_route)-1))
    overall_total_cost += individual_cost
    
    # Re-map to original city IDs including depot
    original_city_ids = [0] + [i+1 for i in range(len(cities)) if assignments[i] == robot_id]
    tour = [original_city_ids[i] for i in optimized_route_indices] + [0]
    
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {individual...

# Print the overall cost
print(f"Overall Total Travel Cost: {overall_total$('#emotion#relief')or_total_cost}")