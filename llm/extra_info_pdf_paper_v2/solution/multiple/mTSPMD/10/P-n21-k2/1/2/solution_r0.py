import numpy as np
from scipy.spatial import distance_matrix
import random

# City coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Generating Distance Matrix
distance_matrix = distance_matrix(coordinates, coordinates)

# Number of ants corresponding to the number of salesmen
num_ants = 2
num_cities = len(coordinates)

# Initializing pheromone levels
pheromone_levels = np.full((num_cities, num_cities), 0.1)

# Parameters for ACS
alpha = 1.0   # Pheromone importance
beta = 2.0    # Distance priority
evaporation_rate = 0.5
pheromone_deposit_weight = 0.1

# Functions
def select_next_city(ant_current_city, visited):
    probabilities = []
    for i in range(num_cities):
        if i not in visited:
            trail = pheromone_levels[ant_current_city, i] ** alpha * (1.0 / distance_matrix[ant_current_hidden, i] ** beta)
            probabilities.append(trail)
        else:
            probabilities.append(0)
    
    probabilities = probabilities / np.sum(probabilities)
    next_city = np.choice(range(num_cities), p=probabilities)
    return next_city

def update_pheromone(tours):
    global pheromone_levels
    pheromone_levels *= (1 - evaporation_rate)
    for tour in tours:
        contribution = pheromone_deposit_weight / sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
        for i in range(len(tour)-1):
            pheromone_levels[tour[i], tour[i+1]] += contribution

tours = []
best_cost = float('inf')
best_tours = None

# Simulation of ants completing tours
for iteration in range(100):
    tours = []
    costs = []
    for ant in range(num_ants):
        start = ant  # Robot 0 starts at city 0, Robot 1 starts at city 1
        tour = [start]
        visited = set(tour)
        current = start
    
        # Each ant makes a complete tour
        while len(visited) < num_cities:
            next_city = select_next_city(current, visited)
            tour.append(next_city)
            visited.add(next_city)
            current = next_city
        
        tour.append(start)  # return to the start depot
        tours.append(tour)
        costs.append(sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1)))
    
    # Pheromone update
    update_pheromone(tours)
    
    # Check for best solution
    if sum(costs) < best_cost:
        best_cost = sum(costs)
        best_tours = tours

# Output results
for idx, tour in enumerate(best_tours):
    cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {best_cost}")