import math
from scipy.spatial.distance import euclidean
from itertools import permutations

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robots info
num_robots = 8
robot_capacity = 40

def calc_distance(coord1, coord2):
    return euclidean(coord1, coord2)

# Clustering function
def cluster_cities(demands, capacities):
    clusters = []
    current_cluster = []
    current_capacity = 0
    
    for i in range(1, len(demands)):  # Start from 1 to avoid the depot city
        if current_capacity + demands[i] <= capacities:
            current_cluster.append(i)
            current_capacity += demands[i]
        else:
            clusters.append(current_cluster)
            current_cluster = [i]
            current_capacity = demands[i]
    
    if current_cluster:
        clusters.append(current_cluster)

    # Handle cases with fewer clusters than robots (idly assign empty clusters)
    while len(clusters) < num_robots:
        clusters.append([])

    return clusters

# Solves TSP within each cluster
def tsp_route(cluster, depot):
    min_route = None
    min_distance = float('inf')
    
    for perm in permutations(cluster):
        route = [depot] + list(perm) + [depot]
        distance = sum(calc_distance(coordinates[route[j]], coordinates[route[j + 1]]) for j in range(len(route) - 1))
        
        if distance < min_distance:
            min_route = route
            min_distance = distance
    
    return min_route, min_distance

clusters = cluster_cities(demands, robot_capacity)
robot_tours = []
total_cost = 0

# Generate and evaluate routes for each robot
for i, cluster in enumerate(clusters):
    if cluster:
        route, route_cost = tsp_route(cluster, 0)
        robot_tours.append((route, route_cost))
        total_cost += route_cost
    else:
        robot_tours.append(([0, 0], 0))

# Output the tours and costs
for i, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print("Overall Total Travel Cost:", total_cost)