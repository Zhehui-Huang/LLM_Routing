import math
import numpy as np

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

# Parameters
num_robots = 4
capacity = 6000
num_cities = len(coordinates)

# Calculate the Euclidean distance matrix
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Heuristic greedy tour partition (simplified version just for demonstration purposes)
def greedy_tour():
    remaining_demand = demands[1:]  # excluding depot
    remaining_cities = list(range(1, num_cities))
    routes = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    
    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            for city in remaining_cities:
                if loads[robot] + remaining_demand[city - 1] <= capacity:
                    if not routes[robot]:  # if the route is empty
                        routes[robot].extend([0, city, 0])  # start from depot
                    else:
                        routes[robot].insert(-1, city)  # add before the return to depot
                    loads[robot] += remaining_demand[city - 1]
                    remaining_cities.remove(city)
                    break
                
    return routes

# Initialize tours
routes = greedy_tour()

# Calculate costs and display output
def calculate_costs_and_output(routes):
    total_cost = 0
    outputs = []
    
    for idx, route in enumerate(routes):
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_cost += cost
        outputs.append(f"Robot {idx} Tour: {route}")
        outputs.append(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    
    outputs.append(f"Overall Total Travel Cost: {total_cost:.2f}")
    return outputs

# Output
output_data = calculate_costs_and_output(routes)
for line in output_frame:
    print(line)