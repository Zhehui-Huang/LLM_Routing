import numpy as np
import random
import math

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1
alpha = 1
beta = 2
rho = 0.1
num_cities = len(city_coords)
robots = [0, 1]  # Depot indices for robots

# Function to calculate Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0])**2 + (city_coords[i][1] - city_coords[j][1])**2)

# Initialize pheromone levels
pheromones = np.full((num_cities, num_cities), inittrail)
heuristic = np.zeros((num_cities, num_cities))

# Calculate heuristic information based on distances
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            heuristic[i, j] = 1.0 / euclidean_dist(i, j)

# Main ACO
def ant_colony_optimization():
    best_cost = float('inf')
    best_solution = None
    
    for cycle in range(cyclenum):
        solutions = []
        costs = []
        
        for _ in range(antnum):
            solution, cost = construct_solution()
            solutions.append(solution)
            costs.append(cost)
        
        # Update pheromones
        pheromones *= (1 - rho)  # Evaporation
        for i, solution in enumerate(solutions):
            for j in range(len(solution) - 1):
                a, b = solution[j], solution[j + 1]
                pheromones[a, b] += 1 / costs[i]  # Deposition
        
        # Check for new best solution
        cycle_best_cost = min(costs)
        if cycle_best_cost < best_cost:
            best_cost = cycle_best_cost
            best_solution = solutions[costs.index(cycle_best_cost)]
        
    return best_solution, best_cost

# Solution construction by an ant
def construct_solution():
    robot_route = {0: [0], 1: [1]}  # Start at respective depots
    unvisited = set(range(2, num_cities))
    
    current_location = {0: 0, 1: 1}
    
    while unvisited:
        for robot in robots:
            possible_moves = [(city, heuristic[current_location[robot], city] * (pheromones[current_location[robot], city])**alpha) for city in unvisited]
            if possible_moves:
                next_city = select_next_city(possible_moves)
                robot_route[robot].append(next_city)
                current_location[robot] = next_city
                unvisited.remove(next_city)
    
    # Complete tours for each robot
    for robot in robots:
        robot_route[robot].append(robot_route[robot][0])  # Return to depot
    
    # Calculate costs
    total_cost = 0
    costs = {}
    for robot, route in robot_route.items():
        cost = sum(euclidean_dist(route[i], route[i+1]) for i in range(len(route) - 1))
        costs[robot] = cost
        total_cost += cost

    return robot_route, costs, total_cost

def select_next_city(possible_moves):
    total = sum(weight for _, weight in possible_moves)
    r = random.uniform(0, total)
    cum_sum = 0
    for city, weight in possible_moves:
        cum_sum += weight
        if cum_sum >= r:
            return city

# Run optimization
solution, cost = ant_colony_optimization()

# Output Results
for robot, route in solution.items():
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {cost[robot]}")

print(f"Overall Total Travel Domain: {sum(cost.values())}")