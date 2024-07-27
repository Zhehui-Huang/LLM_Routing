import numpy as np
import math
from random import choice

# City coordinates provided in the problem statement
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
depot_indices = list(range(8))

# Algorithm parameters
antnum = 20
cyclenum = 100
init_pheromone = 1.0
alpha = 1.0
beta = 5.0
rho = 0.1

# Calculate distance matrix using Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = [
    [calculate_distance(cities[i], cities[j]) for j in range(len(cities))] 
    for i in range(len(cities))
]

# Initialize pheromones
pheromones = [
    [init_pheromone for _ in range(len(cities))] 
    for _ in range(len(cities))
]

# Heuristic information: Inverse of distances
heuristic = [
    [1 / distances[i][j] if i != j else 0 for j in range(len(cities))] 
    for i in range(len(cities))
]

def create_solution():
    tours = {robot: [depot] for robot, depot in enumerate(depot_indices)}
    cost = {robot: 0 for robot in range(len(depot_indices))}
    remaining_cities = set(range(len(cities))) - set(depot_indices)
    
    while remaining_cities:
        for robot in tours:
            if remaining_cities:
                current_city = tours[robot][-1]
                probabilities = [
                    (pheromones[current_city][next_city] ** alpha) * (heuristic[current_city][next_city] ** beta)
                    if next_city in remaining_cities else 0
                    for next_city in range(len(cities))
                ]
                next_city = np.random.choice(len(cities), p = np.array(probabilities) / sum(probabilities))
                tours[robot].append(next_city)
                cost[robot] += distances[current_city][next_city]
                remaining_cities.remove(next_city)
    for robot, depot in enumerate(depot_indices):
        last_city = tours[robot][-1]
        tours[robot].append(depot)
        cost[robot] += distances[last_city][depot]

    return tours, cost

def update_pheromones(all_tours, all_costs):
    for i in range(len(cities)):
        for j in range(len(cities)):
            pheromones[i][j] *= (1 - rho)
    
    for robot, tour in all_tours.items():
        contribution = 1 / all_costs[robot]
        for i in range(len(tour) - 1):
            pheromones[tour[i]][tour[i+1]] += contribution

# Main simulation loop
best_solution = None
best_cost = float('inf')

for _ in range(cyclenum):
    all_tours, all_costs = create_solution()
    current_cost = sum(all_costs.values())
    if current_cost < best_cost:
        best_cost = current_tour
        best_cost = current_cost
    update_pheromones(all_tours, all_costs)

# Output results
for robot, tour in best_solution.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {best_cost[robot]}")
print(f"Overall Total Travel Cost: {sum(best_cost.values())}")