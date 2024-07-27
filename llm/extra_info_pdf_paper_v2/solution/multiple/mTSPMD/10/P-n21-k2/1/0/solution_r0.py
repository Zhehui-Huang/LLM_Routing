import numpy as np
import random

# Given city coordinates (indices are aligned with city IDs)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Adjacency matrix of distances
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_model(coordinates[i], coordinates[j])

# Ant Colony Optimization Parameters
num_ants = 50
num_iterations = 100
pheromone_evaporation_coeff = 0.5
pheromone_constant = 1000
alpha = 1  # influence of pheromone on direction
beta = 2   # influence of heuristic value (inverse of distance)

# Pheromone matrix
pheromone_levels = np.ones((num_cities, num_cities))

def choose_next_city(current_city, visited):
    probabilities = []
    for city in range(num_cities):
        if city not in visited:
            pheromone = pheromone_levels[current_city][city] ** alpha
            heuristic = (1 / distance_matrix[current_city][city]) ** beta
            probabilities.append(pheromone * heuristic)
        else:
            probabilities.append(0)
    
    probabilities = probabilities / np.sum(probabilities)
    next_city = np.random.choice(range(num_cities), p=probabilities)
    return next_city

def calculate_tour_length(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def ant_colony_optimization():
    best_length = float('inf')
    best_tour = None
    
    for iteration in range(num_iterations):
        for ant in range(num_ants):
            tour = [np.random.randint(0, num_cities)]
            while len(tour) < num_cities:
                next_city = choose_next_city(tour[-1], tour)
                tour.append(next_city)
            tour.append(tour[0])  # Return to start
            
            # Evaluate tour
            length = calculate_tour_length(tour)
            if length < best_length:
                best_length = length
                best_tour = tour
            
            # Pheromone update
            for i in range(len(tour) - 1):
                delta_pheromone = pheromone_constant / length
                pheromone_levels[tour[i]][tour[i + 1]] += delta_pheromone
        
        # Pheromone evaporation
        pheromone_levels *= (1 - pheromone_evaporation_coeff)
    
    return best_tour, best_length

# Running the ACO to find the best tours for both robots
best_tour, best_length = ant_colony_optimization()

# Splitting the tour into two based on depot assignments
# Simplistic split: Based on the position in the list of tours
mid_point = len(best_totur) // 2
robot_0_tour = best_totur[:mid_point] + [0]  # Assuming robot 0 returns to depot 0
robot_1_tour = best_totur[mid_point:] + [1]  # Assuming robot 1 returns to depot 1

robot_0_cost = calculate_tour_length(robot_0_tour)
robot_1_cost = calculate_tour_length(robot_1_tour)

# Output
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", robot_0_cost + robot_1_cost)