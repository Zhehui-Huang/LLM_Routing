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

distances = calc_distances(coordinates)

# Function to assign cities to robots such that each robot's load does not exceed its capacity
def assign_cities_to_robots(demands, capacity, num_robots):
    num_cities = len(demands)
    city_indices = list(range(1, num_cities))  # Exclude the depot
    tours = [[] for _ in range(num_robots)]
    city_assignments = [-1] * num_cities
    loads = [0] * num_robots
    
    sorted_cities = sorted(city_indices, key=lambda x: -demands[x])
    
    for city in sorted_cities:
        for robot in range(num_robots):
            if loads[robot] + demands[city] <= capacity:
                tours[robot].append(city)
                loads[robot] += demands[city]
                city_assignments[city] = robot
                break
            
    return tours

# Get raw tours and their assignments
raw_tours = assign_cities_to_robots(demands, capacity, num_robots)

# Function to find the optimal round trip for each tour
def optimal_round_trip(tour, dist_matrix):
    if not tour:
        return [0, 0], 0  # Return to depot if no cities in the tour
    best_path = None
    best_cost = float('inf')
    all_permutations = permutations(tour)
    for perm in all_permutations:
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < best_cost:
            best_cost = cost
            best_path = path
    return best_path, best_cost

# Calculate and optimize the tours and total travel cost
overall_total_cost = 0
for i, tour in enumerate(raw_tours):
    opt_tour, tour_cost = optimal_round_trip(tour, distances)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {opt_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")