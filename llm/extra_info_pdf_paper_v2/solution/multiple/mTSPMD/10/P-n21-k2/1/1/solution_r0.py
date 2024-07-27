import numpy as np
import random

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters for ACO
num_ants = 20
num_iterations = 100
decay = 0.5
alpha = 1
beta = 2
initial_pheromone = 1.0 / len(cities)

# Calculate distances between all pairs of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
                distances[i][j] = dist
            else:
                distances[i][j] = float('inf')  # No self-loop
    return distances

# Initialize pheromones
def initialize_pheromones(num_cities, initial_value):
    return np.full((num_cities, num_cities), initial_value)

# Ant colony optimization function
def ant_colony_optimization(start_points, distances, num_ants, num_iterations, decay, alpha, beta):
    num_cities = len(cities)
    pheromones = initialize_pheromones(num_cities, initial_pheromone)
    all_time_best_cost = float('inf')
    all_time_best_path = []

    for iteration in range(num_iterations):
        paths = []
        costs = []
        
        for ant in range(num_ants):
            path = [random.choice(start_points)]
            while len(set(path)) < num_cities:
                current = path[-1]
                probabilities = []
                 # Calculate transition probabilities
                for city in range(num_cities):
                    if city not in path:
                        trail = (pheromones[current][city] ** alpha) * ((1 / distances[current][city]) ** beta)
                    else:
                        trail = 0
                    probabilities.append(trail)
                probabilities = probabilities / np.sum(probabilities)
                next_city = int(np.random.choice(range(num_cities), 1, p=probabilities))
                path.append(next_city)

            path.append(path[0])  # return to the starting city
            costs.append(sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1)))
            paths.append(path)
            
            # Update the best cost
            current_cost = costs[-1]
            if current_cost < all_time_best_cost:
                all_time_best_cost = current_cost
                all_time_best_path = path[:-1] 
        
        # Pheromone evaporation and update
        pheromones = (1 - decay) * pheromones
        for idx, path in enumerate(paths):
            for i in range(len(path) - 1):
                pheromones[path[i]][path[i + 1]] += 1 / costs[idx]

    return all_time_best_path, all_time_best_cost

distances = calculate_distances(cities)

# Define start points for each robot
robot_start_points = [0, 1]

# Run the optimization
best_path, best_cost = ant_colon