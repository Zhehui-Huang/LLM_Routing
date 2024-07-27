import numpy as np
import random

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 5.0
rho = 0.5

# Pheromone initialization
pheromones = np.full((len(city_coords), len(city_coords)), inittrail, dtype=float)

def euclidean_distance(c1, c2):
    return np.linalg.norm(np.array(c1) - np.array(c2))

# Initialize heuristic information (inverse of distance)
eta = np.zeros((len(city_coords), len(city_coords)))
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i != j:
            eta[i][j] = 1.0 / euclidean_distance(city_coords[i], city_coords[j])

def construct_solution(allowed, start_depot):
    tour = [start_depot]
    current_city = start_depot
    while len(allowed) > 0:
        probabilities = []
        for j in allowed:
            probability = (pheromones[current_city][j] ** alpha) * (eta[current_city][j] ** beta)
            probabilities.append(probability)
        probabilities = np.array(probabilities) / sum(probabilities)
        next_city = np.random.choice(allowed, p=probabilities)
        tour.append(next_city)
        allowed.remove(next_city)
        current_city = next_city
    tour.append(start_depot) # Return to the depot
    return tour

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return cost

# Main ACO loop
best_solution = None
best_cost = float('inf')
stagnant_cycles = 0

for cycle in range(cyclenum):
    solutions = []
    costs = []
    for ant in range(antnum):
        if ant % 2 == 0:
            start_depot = 0 # Robot 0 starts at depot city 0
        else:
            start_depot = 1 # Robot 1 starts at depot city 1
        allowed_cities = list(range(len(city_coords)))
        allowed_cities.remove(start_depot)
        
        solution = construct_solution(allowed_cities, start_deport)
        cost = calculate_tour_cost(solution)
        solutions.append(solution)
        costs.append(cost)
    
    if min(costs) < best_cost:
        best_solution = solutions[costs.index(min(costs))]
        best_cost = min(costs)
        stagnant_cycles = 0
    else:
        stagnant_cycles += 1
    
    # Update pheromones
    pheromones *= (1 - rho) # Evaporation
    for i, solution in enumerate(solutions):
        for j in range(1, len(solution)):
            pheromones[solution[j-1]][solution[j]] += 1 / costs[i]
    
    if stagnant_cycles >= cyclenum:
        break

# Output the best solution details
if best_solution is not None:
    print(f"Best Solution Tour: {best_solution}")
    print(f"Total Travel Cost: {best_cost}")