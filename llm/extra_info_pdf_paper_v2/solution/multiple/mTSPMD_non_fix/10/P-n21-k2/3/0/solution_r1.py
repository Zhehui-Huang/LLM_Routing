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

# Simulated Annealing Setup
T = 1000  # Starting temperature
T_min = 1  # Minimum temperature
alpha = 0.99  # Cooling rate

def simulated_annealing(cities):
    current_solution = cities[:]
    best_solution = cities[:]
    best_cost = calculate_total_distance(best_solution)
    
    temperature = T
    while temperature > T_min:
        neighbor = create_neighbor(current_solution)
        current_cost = calculate_total_cv_total
        neighbor_cost = calculate_total_distance(neighbor)
        
        if neighbor_cost < current_cost or random.random() < math.exp((current_cost - neighbor_cost) / temperature):
            current_solution = neighbor[:]
            if neighbor_cost < best_cost:
                best_solution = neighbor[:]
                best_cost = neighbor_cost
        
        temperature *= alpha

    return best_solution, best_cost

def create_neighbor(solution):
    idx1, idx2 = random.sample(range(1, len(solution) - 1), 2)  # Exclude depots in swaps
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

def calculate_total_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += distance_matrix[route[i - 1], route[i]]
    total_distance += distance_matrix[route[-1], route[0]]  # Return to depot
    return total_distance

# Split cities between robots, avoiding depots, and include return in the simulated annealing
remaining_cities = list(range(2, 21))
random.shuffle(remaining_cities)
split_index = len(remaining_cities) // 2

robot_0_cities = [0] + remaining_cities[:split_index] + [0]
robot_1_cities = [1] + remaining_cities[split_index:] + [1]

# Perform Simulated Annealing for each robot
robot_0_route, robot_0_cost = simulated_annealing(robot_0_cities)
robot_1_route, robot_1_cost = simulated_annealing(robot_1_cities)
overall_cost = robot_0_cost + robot_1_cost

# Display the output
print("Robot 0 Tour:", robot_0_route)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_route)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", overall_cost)