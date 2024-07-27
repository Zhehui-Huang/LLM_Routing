import numpy as np
import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), # Depot for robot 0
    1: (37, 52), # Depot for robot 1
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of ants and cycles
antnum = 10
cyclenum = 100

# ACO parameters
alpha = 1
beta = 5
rho = 0.1

# Initialize distances and heuristic information
distances = {}
heuristic_info = {}

number_of_cities = len(cities)
for i in range(number_of_cities):
    distances[i] = {}
    heuristic_info[i] = {}
    for j in range(number_of_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])
        heuristic_info[i][j] = 1 / (distances[i][j] + 1e-5)  # Avoid division by zero

# Initialize pheromones
pheromones = {}
for i in range(number_of_cities):
    pheromones[i] = {j: 1.0 for j in range(number_of_cities)}

def select_next_city(current_city, allowed_cities):
    probabilities = []
    denom = sum((pheromones[current_city][j]**alpha) * (heuristic_info[current_city][j]**beta) for j in allowed_cities)
    for j in allowed_cities:
        if denom == 0:
            probabilities.append(0)
        else:
            prob = (pheromones[current_city][j]**alpha * heuristic_info[current_city][j]**beta) / denom
            probabilities.append(prob)
    next_city = np.random.choice(allowed_cities, p=np.array(probabilities)/sum(probabilities))
    return next_city

# Simulation
best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    solutions = []
    for ant in range(antnum):
        solution = {}
        solution[0] = [0]  # Robot 0 starts at depot 0
        solution[1] = [1]  # Robot 1 starts at depot 1
        remaining_cities = set(cities.keys()) - {0, 1}
        
        # Build the solution for each robot
        for robot_id in range(2):
            current_city = solution[robot_id][-1]
            while remaining_cities:
                allowed_cities = list(remaining_cities)
                next_city = select_next_city(current_city, allowed_cities)
                solution[robot_id].append(next_city)
                current_city = next_city
                remaining_cities.remove(next_city)
        
            # Return to the respective depots
            solution[robot_id].append(robot_id)

        # Evaluate solution
        total_cost = 0
        for robot_id in range(2):
            tour_cost = sum(distances[solution[robot_id][i]][solution[robot_id][i + 1]] for i in range(len(solution[robot_id]) - 1))
            total_cost += tour_cost
        
        solutions.append((solution, total_cost))

        if total_cost < best_cost:
            best_cost = total_cost
            best_solution = solution

    # Pheromone update
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            pheromones[i][j] *= (1 - rho)
    
    for solution, cost in solutions:
        for robot_id in range(2):
            for i in range(len(solution[robot_id]) - 1):
                i1 = solution[robot_id][i]
                i2 = solution[robot_id][i + 1]
                pheromones[i1][i2] += 1.0 / cost

# Output the results
overall_total_travel_cost = 0
for robot_id in range(2):
    tour = best_solution[robot_id]
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    overall_total_travel_cost += tour_cost
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {overall_total_travel_cost}')