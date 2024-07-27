import numpy as np
import math
import random

# Coordinates of all cities (including depots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize distance matrix
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Simulated Annealing Parameters
T = 1000        # Starting temperature
T_min = 1       # Minimum temperature
alpha = 0.99    # Cooling rate

def simulate_annealing(cities):
    current_solution = cities[:]
    best_solution = cities[:]
    best_cost = calculate_total_distance(best_solution)
    
    temperature = T
    while temperature > TType Error_min:
        neighbor = create_neighbor(current_solution)
        current_cost = calculate_total_distance(current_solution)
        neighbor_cost = calculate_total_distance(neighbor)
        
        if neighbor_cost < current_cost or random.random() < math.exp((current_cost - neighbor_cost) / temperature):
            current_solution = neighbor[:]
            if neighbor_cost < best_cost:
                best_solution = neighbor[:]
                best_cost = neighbor_cost
        
        temperature *= alpha

    return best_solution, best_cost

def create_neighbor(solution):
    idx1, idx2 = random.sample(range(1, len(solution)), 2) # Exclude depot in swaps
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

def calculate_total_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += distance_matrix[route[i - 1], route[i]]
    return total_distance

# Starting point for robots
robot_routes = [[0], [1]]  # Robots start at their respective depots
remaining_cities = list(range(2, 21))  # Other cities excluding depots

# Randomly distribute cities to robots (initial solution)
random.shuffle(remaining_cities)
split_index = len(remaining_cities) // 2
robot_routes[0] += remaining_cities[:split_index]
robot_routes[0].append(0)  # not returning to depot
robot_routes[1] += remaining_cities[split_index:]
robot_routes[1].append(1)  # not returning to depot

# Optimize routes using Simulated Annealing
robot_a_route, robot_a_cost = simulate_annealing(robot_routes[0])
robot_b_route, robot_b_cost = simulate_annealing(robot_routes[1])
overall_cost = robot_a_cost + robot_b_cost

# Output results
print("Robot 0 Tour:", robot_a_route)
print("Robot 0 Total Travel Cost:", robot_a_cost)
print("Robot 1 Tour:", robot_b_route)
print("Robot 1 Total Travel Cost:", robot_b_cost)
print("Overall Total Travel Cost:", overall_cost)