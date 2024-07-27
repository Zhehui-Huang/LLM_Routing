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

# Initialize pheromone levels
pheromones = np.full((len(coordinates), len(coordinates)), init_pheromone)
distances = np.zeros((len(coordinates), len(coordinates)))

# Compute distances
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distances[i][j] = math.dist(coordinates[i], coordinates[j])

# Inverse of distance as heuristic
heuristic = 1 / (distances + 1e-5)  # Add small epsilon to avoid division by zero

def choose_next_city(current_city, allowed_cities):
    pheromone_current = pheromones[current_city, allowed_cities]
    heuristic_current = heuristic[current_city, allowed_cities]
    probabilities = (pheromone_current ** alpha) * (heuristic_current ** beta)
    probabilities /= probabilities.sum()
    next_city_idx = np.random.choice(range(len(allowed_cities)), p=probabilities)
    return allowed_cities[next_city_idx]

def compute_tour_cost(tour):
    tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return tour_cost

best_solution = None
best_solution_cost = float('inf')
no_improvement_cycles = 0

for cycle in range(num_cycles):
    all_ants_solutions = []
    all_ants_costs = []
    
    for ant in range(num_ants):
        start_depot = random.choice([0, 1])  # Choose a random depot to start
        tour = [start_depot]
        remaining_cities = set(range(2, len(coordinates)))  # All cities except depots
        
        while remaining_cities:
            current_city = tour[-1]
            allowed_cities = list(remaining_cities - {current_city})
            if allowed_cities:
                next_city = choose_next_city(current_city, allowed_cities)
                tour.append(next_city)
                remaining_cities.remove(next_city)
            else:
                break
        # Return to start depot
        tour.append(start_depot)
        
        tour_cost = compute_tour_cost(tour)
        all_ants_solutions.append(tour)
        all_ants_costs.append(tour_cost)
    
    # update pheromones
    pheromones *= (1 - rho)  # Evaporation
    for ant_idx, (ant_tour, cost) in enumerate(zip(all_ants_solutions, all_ants_costs)):
        for i in range(len(ant_tour) - 1):
            pheromones[ant_tour[i], ant_tour[i + 1]] += 1 / cost
    
    # determine the best solution in this cycle
    min_cost_idx = np.argmin(all_ants_costs)
    min_cost = all_ants_costs[min_cost_idx]
    if min_cost < best_solution_cost:
        best_solution = all_ants_solutions[min_cost_idx]
        best_solution_cost = min_cost
        no_improvement_cycles = 0
    else:
        no_improvement_cycles += 1
    
    if no_improvement_cycles >= cyclenum:
        break

# Separate tours for each robot
robot_0_tour = [idx for idx in best_solution if best_solution.index(idx) % 2 == 0]
robot_1_tour = [idx for idx in best_solution if best_solution.index(idx) % 2 != 0]

robot_0_cost = compute_tour_cost(robot_0_tour)
robot_1_cost = compute_tour_cost(robot_1_tour)

# Present results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", robot_0_cost + robot_1_cost)