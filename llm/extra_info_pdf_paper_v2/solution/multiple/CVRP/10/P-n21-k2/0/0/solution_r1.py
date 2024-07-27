import math
from itertools import combinations

# Cities coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 81), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
num_cities = len(coordinates)
robot_capacity = 160
num_robots = 2

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Calculate savings considering the depot (city 0) and other city pairs
savings_list = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        savings = euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)
        savings_list.append((savings, i, j))

# Sort savings in descending order
savings_list.sort(reverse=True, key=lambda x: x[0])

# Initialize routes as clusters
clusters = [[i] for i in range(1, num_cities)]
cluster_load = [demands[i] for i in range(num_cities)]  # hold associated demands/load for each cluster

# Clarke and Wright Savings Algorithm - Merge
while savings_list:
    savings, i, j = savings_list.pop(0)
    cluster_i = next((c for c in clusters if i in c), None)
    cluster_j = next((c for c in clusters if j in c), None)
    
    if cluster_i != cluster_preview, ini":"k the peak or black&white motion and capture timetion
    if cluster_i and cluster_j and cluster_i != cluster_j:
        if cluster_load[clusters.index(cluster_i)] + cluster_load[clusters.index(cluster_j)] <= robot_capacity:
            # merge clusters
            clusters.remove(cluster_i)
            clusters.remove(cluster_j)
            new_cluster = cluster_i + cluster_j
            clusters.append(new_cluster)
            cluster_load.append(cluster_load.pop(clusters.index(cluster_i)) + cluster_load.pop(clusters.index(cluster_j)))
            cluster_load.pop(-1)

# Create tours for robots
routes = [[0] + cluster + [0] for cluster in clusters if cluster]
routes = sorted(routes, key=lambda x: sum(euclidean_distance(x[i], x[i+1]) for i in range(len(x)-1)))

# Distribute routes to the robots
assigned_routes = [[] for _ in range(num_robots)]
route_costs = [0 for _ in range(num_robots)]
idx = 0

for route in routes:
    assigned_routes[idx].append(route)
    route_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))
    route_costs[idx] += route_cost
    idx = (idx + 1) % num_robots

# Outputting results
total_cost = 0
for i in range(num_robots):
    print(f'Robot {i} Tour: {assigned_routes[i]}')
    print(f'Robot {i} Total Travel Cost: {route_costs[i]}')
    total_cost += route_costs[i]

print(f'Overall Total Travel Cost: {total_cost}')