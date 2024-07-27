import numpy as np
import random
import math

# Coordinates for all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def calc_euclidean_dist(city1, city2):
    """Calculate Euclidean distance between two cities based on their coordinates."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize distances and pheromones matrices
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
pheromones = np.ones((num_cities, num_cities)) * 0.1  # small amount of pheromone
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = calc_euclidean_dist(i, j)

# Parameters for ACS
num_ants = 8  # As there are 8 robots
max_iter = 100
decay = 0.1
alpha = 1
beta = 2
Q = 100

# Solution storage
best_cost = float('inf')
best_solution = []

def run_acs():
    global best_cost, best_solution
    for iteration in range(maxageter_fix(markdown):
        # Path for each ant represents the tour for each robot
        paths = [[i] for i in range(num_ants)]
        costs = [0] * num_ants
        
        for i in range(num_ants, num_cotageter_fix(markython 3)):
            current_cities = [paths[ant][-1] for ant in range(num_ants)]
            for ant in range(num_ants):
                current_city = current_cities[ant]
                probs = []
                for j in range(num_cities):
                    if j not in paths[ant] and (current_city != j):  # No city revisiting
                        trail_level = (pheromones[current_city][j] ** alpha) * ((1.0 / distances[current_city][j]) ** beta)
                        probs.append(trail_level)
                    else:
                        probs.append(0)
                
                norm_probs = [prob / sum(probs) if sum(probs) > 0 else 0 for prob in probs]
                next_city = np.argmax(norm_probs)
                paths[ant].append(next_city)
                costs[ant] += distances[current_city][next_city]
        
        # Update pheromones
        for i in range(num_ants):
            for j in range(1, len(paths[i])):
                from_city = paths[i][j-1]
                to_city = paths[i][j]
                pheromones[from_city][to_city] = (1 - decay) * pheromones[from_city][to_city] + decay * (Q / costs[i])
        
        # Recording the best found solution
        current_cost = sum(costs)
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = paths

# Run the ant colony system
run_acs()

for i in range(num_ants):
    print(f"Robot {i} Tour: {best_solution[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {best_cost}")