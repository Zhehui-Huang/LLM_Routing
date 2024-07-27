import numpy as np
from scipy.spatial import distance_matrix
from collections import defaultdict

# Coordinates and demands
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
               (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
               (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
               (164, 193), (129, 189), (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Parameters
num_robots = 4
robot_capacity = 6000

# Distance Calculation
dist_matrix = distance_matrix(coordinates, coordinates)

# Cluster Assignment (Greedy Bin Packing for Capacitated Vehicle Routing Problem)
city_indices = list(range(1, len(coordinates)))  # exclude the depot 0
city_demand_pairs = sorted(zip(city_indices, demands[1:]), key=lambda x: x[1], reverse=True)

assignments = defaultdict(list)
capacities = defaultdict(int)
for city, demand in city_demand_pairs:
    assigned = False
    for robot in range(num_robots):
        if capacities[robot] + demand <= robot_capacity:
            assignments[robot].append(city)
            capacities[robot] += demand
            assigned = True
            break

    if not assigned:
        # If no robot can take this demand alone at this stage, it's a problem.
        raise Exception("Capacity too low or single city demand too high for all robots!") 

# TSP Route per Robot (Greedy Nearest Neighbor per cluster)
def greedy_tsp(tour, dist_matrix):
    unvisited = set(tour)
    path = [0]  # start at depot
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        path.append(next_service_city)
        unvisited.remove(next)
        current = next_city
    path.append(0)  # return to depot
    return path

routes = {}
total_costs = 0

for robot, cities in assignments.items():
    route = greedy_tsp(cities, dist_matrix)
    routes[robot] = route
    route_cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_costs += route_cost
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_costs:.2f}")