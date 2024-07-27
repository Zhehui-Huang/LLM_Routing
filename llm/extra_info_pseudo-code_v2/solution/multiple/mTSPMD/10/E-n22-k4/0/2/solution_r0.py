import numpy as np
import random

# Coordinates of cities
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Parameters for ACO
alpha = 1.0
beta = 5.0
rho = 0.5
init_pheromone = 0.1
antnum = 20
cyclenum = 100

# Compute Euclidean distance between two cities
def euc_distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Initialize pheromone levels
def initialize_pheromones(n, initial):
    return np.full((n, n), initial)

# Make a move: choose the next city
def select_next_city(current_city, allowed_cities, pheromone, distances, alpha, beta):
    pheromones = np.array([pheromone[current_city][j]**alpha for j in allowed_cities])
    visibilities = np.array([1.0 / distances[current_city][j]**beta for j in allowed_cities])
    probabilities = pheromones * visibilities
    probabilities /= probabilities.sum()
    next_city = np.random.choice(allowed_cities, p=probabilities)
    return next_city

# Update pheromones
def update_pheromones(pheromone, ants, rho):
    pheromone *= (1 - rho)  # Evaporation
    for ant in ants:
        contribution = 1.0 / ant['cost'] 
        for i, j in zip(ant['tour'], ant['tour'][1:] + [ant['tour'][0]]):
            pheromone[i][j] += contribution
            pheromone[j][i] += contribution  # because the graph is undirected

# Function to simulate the ants finding tours
def ant_colony_optimization():
    num_cities = len(cities)
    distances = np.array([[euc_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])
    pheromone = initialize_pheromones(num_cities, init_pheromone)
    
    best_cost = float('inf')
    best_solution = None

    for cycle in range(cyclenum):
        ants = [{'tour': [i], 'cost': 0.0} for i in range(4)]  # Start each robot at its depot
        for _ in range(num_cities - 1):
            for ant in ants:
                if len(ant['tour']) < num_cities:
                    current_city = ant['tour'][-1]
                    allowed_cities = [j for j in range(num_cities) if j not in ant['tour']]
                    if allowed_cities:
                        next_city = select_next_city(current_city, allowed_cities, pheromone, distances, alpha, beta)
                        ant['tour'].append(next_city)
                        ant['cost'] += distances[current_city][next_city]
                    # Return to start depot
                    ant['tour'].append(ant['tour'][0])
                    back_cost = distances[current_city][ant['tour'][0]]
                    ant['cost'] += back_cost
        
        # Update the best solution found
        for ant in ants:
            if ant['cost'] < best_cost:
                best_cost = ant['cost']
                best_solution = ant['tour']
        
        # Update pheromones
        update_pheromones(pheromone, ants, rho)

    return best_solution, best_cost

best_tour, best_total_cost = ant_colony_optimization()
print(f"Best Tour: {best_tour}")
print(f"Best Total Travel Cost: {best_total_cost}")