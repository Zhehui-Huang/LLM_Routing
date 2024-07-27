import numpy as np
import random
import math

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Parameters
num_ants = 10
num_cycles = 100
init_pheromone = 1
alpha = 1
beta = 5
rho = 0.1
cyclenum = 20

# Initialize pheromone levels and compute distances
pheromones = np.ones((len(coordinates), len(coordinates))) * init_pheromone
distances = np.array([[math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
                        for j in range(len(coordinates))] for i in range(len(coordinates))])

# Inverse of distance as heuristic
heuristic = 1 / (distances + 1e-10)  # To avoid division by zero

# Choose the next city based on probabilities
def choose_next_city(current_city, allowed_cities):
    pheromone_current = pheromones[current_city][allowed_cities]
    heuristic_current = heuristic[current_city][allowed_cities]
    probabilities = pheromone_current ** alpha * heuristic_current ** beta
    probabilities /= probabilities.sum()
    next_city = np.random.choice(allowed_cities, p=probabilities)
    return next_city

# Compute tour cost
def compute_tour_cost(tour):
    return sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Perform the ant simulation
best_solution = [None, None]
best_solution_cost = [float('inf'), float('inf')]
depots = [0, 1]

for _ in range(num_cycles):
    all_solutions = {0: [], 1: []}
    all_costs = {0: [], 1: []}
    
    for ant in range(num_ants):
        for depot_id in depots:
            tour = [depot_id]
            unvisited = set(range(len(coordinates))) - {depot_id}
        
            while unvisited:
                current_city = tour[-1]
                allowed_cities = list(unvisited)
                next_city = choose_next_city(current_city, allowed_cities)
                tour.append(next_city)
                unvisited.remove(next_city)
            
            # Return to depot
            tour.append(depot_id)
        
            cost = compute_tour_cost(tour)
            all_solutions[depot_id].append(tour)
            all_costs[depot_id].append(cost)
    
    # Check all ant paths at both depots for updates
    for depot_id in depots:
        cycle_best_cost = min(all_costs[depot_id])
        cycle_best_tour = all_solutions[depot_id][all_costs[depot_id].index(cycle_best_cost)]
        
        if cycle_best_cost < best_solution_cost[depot_id]:
            best_solution[depot_id] = cycle_best_tour
            best_solution_cost[depot_id] = cycle_best_cost

    # Pheromone update
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                pheromones[i][j] *= (1 - rho)  # Evaporation
                for depot_id in depots:
                    if [i, j] in [best_solution[depot_id][k:k+2] for k in range(len(best_solution[depot_id]) - 1)]:
                        pheromones[i][j] += 1 / best_solution_cost[depot_id]  # Pheromone deposition

# Display results
total_cost = sum(best_solution_cost)
result = []
for i, depot_id in enumerate(depots):
    result.append(f"Robot {i} Tour: {best_solution[depot_id]}")
    result.append(f"Robot {i} Total Travel Cost: {best_solution_cost[i]}")
result.append(f"Overall Total Travel Cost: {total_cost}")

for line in result:
    print(line)