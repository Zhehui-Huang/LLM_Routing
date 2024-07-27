import numpy as np
from itertools import permutations

# City Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demands
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Number of robots and their capacity
num_robots = 8
capacity = 40

# Calculate Euclidean distances between each pair of cities
def calc_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return dist_matrix

distances = calc_fc_distances(coordinates)

# Function to assign cities to robots such that each robot's load does not exceed its capacity
def assign_cities_to_robots(demands, capacity, num_robots):
    num_cities = len(demands)
    tours = [[] for _ in range(num_robots)]
    current_loads = [0] * num_robots
    city_indices = list(range(1, num_cities))  # city 0 is the depot
    
    # Sort cities based on demands to optimize packing
    sorted_cities = sorted(city_indices, key=lambda x: -demands[x])
    
    for city in sorted_cities:
        for i in range(num_robots):
            if current_loads[i] + demands[city] <= capacity:
                tours[i].append(city)
                current_loads[i] += demands[city]
                break
    
    return tours

# Allocate cities to robots' tours
raw_tours = assign_cities_to_robots(demands, capacity, num_robots)

# Function to find the shortest round trip path for each tour starting and ending at the depot
def optimize_tour(tour, distance_matrix):
    if not tour:
        return [], 0
    best_route = None
    best_cost = float('inf')
    for perm in permutations(tour):
        route = [0] + list(perm) + [0]
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        if cost < best_cost:
            best_cost = cost
            best_route = route
    return best_route, best_cost

# Calculate the optimized tours and their costs
total_cost = 0
optimized_tours = []
for i, tour in enumerate(raw_tours):
    opt_tour, cost = optimize_tour(tour, distances)
    optimized_tours.append(opt_tour)
    total_cost += cost
    print(f"Robot {i} Tour: {opt_tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")