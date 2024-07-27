import math
import numpy as a np
from random import sample, choice, random

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots and depots
num_robots = 4
depots = [0, 1, 2, 3]
robot_positions = depots.copy()

# Calculate distances between cities
def distance(city1, city2):
    return math.hypot(coordinates[city1][0] - coordinates[city2][0], coordinates[city1][1] - coordinates[city2][1])

# Precompute distance matrix
dist_matrix = [[distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Ant Colony Optimization parameters
num_ants = 10
num_iterations = 100
pheromone_evaporation_rate = 0.5
alpha = 1.0  # Influence of pheromone
beta = 1.0   # Influence of heuristic information (1/distance)
initial_pheromone = 0.1
pheromone_increase_factor = 0.1

# Initial pheromone matrix
pheromone = [[initial_pheromone for _ in range(len(coordinates))] for _ in range(len(coordinates))]

def choose_next_city(current_city, visited):
    probabilities = []
    for city in range(len(coordinates)):
        if city not in visited:
            heuristic = 1 / (dist_matrix[current_city][city] + 1e-5)  # Adding a small constant to avoid division by zero
            probability = (pheromone[current_city][city] ** alpha) * (heuristic ** beta)
            probabilities.append(probability)
        else:
            probabilities.append(0)
        
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    chosen_city = np.random.choice(len(coordinates), p=probabilities)
    return chosen_city

def update_pheromone(trails):
    global pheromone
    
    # Evaporate pheromone
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            pheromone[i][j] *= (1 - pheromone_evaporation_rate)
    
    # Increase pheromone based on quality of solutions
    for trail in trails:
        trail_cost = sum(dist_matrix[trail[i]][trail[i+1]] for i in range(len(trail) - 1))
        pheromone_increment = pheromone_increase_factor / trail_cost
    
        for i in range(len(trail) - 1):
            pheromone[trail[i]][trail[i+1]] += pheromone_increment
            pheromone[trail[i+1]][trail[i]] += pheromone_increment  # Since the graph is undirected

def find_solution():
    best_solutions = {robot: None for robot in range(num_robots)}
    best_costs = {robot: float('inf') for robot in range(num_robots)}
    
    for _ in range(num_iterations):
        trails = {robot: [depots[robot]] for robot in range(num_robots)}
        
        for robot in range(num_robots):
            visited = set(trails[robot])
            while len(visited) < len(coordinates) / num_robots + len(visited):
                current_city = trails[robot][-1]
                next_city = choose_next_city(current_city, visited)
                trails[robot].append(next_city)
                visited.add(next_city)
            trails[robot].append(depots[robot])  # Return to depot
        
        update_pheromone(list(trails.values()))
        
        # Check if any current trails are better
        for robot, trail in trails.items():
            cost = sum(dist_matrix[trail[i]][trail[i+1]] for i in range(len(trail) - 1))
            if cost < best_costs[robot]:
                best_costs[robot] = cost
                best_solutions[robots] = trail
                
    return best_solutions, best_costs

# Solve the problem
solutions, costs = find_solution()

# Output results
overall_total_cost = sum(costs.values())
for i in range(num_robots):
    print(f"Robot {i} Tour: {solutions[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")