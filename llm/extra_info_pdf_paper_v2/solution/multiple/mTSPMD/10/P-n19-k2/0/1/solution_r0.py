import numpy as np
import math

# Definitions of cities and their positions
city_coordinates = [
    (30, 40), # Depot for robot 0
    (37, 52), # Depot for robot 1
    (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute distances between all cities
n_cities = len(city_coordinates)
distances = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i, j] = euclidean distance(city_coordinates[i], city_coordinates[j])

# Parameters for ACO
n_ants = 10
n_iterations = 100
pheromone_evaporation_rate = 0.5
pheromone_constant = 1000
alpha = 1  # Influence of pheromone
beta = 5   # Influence of heuristic information

# Initialize pheromones
pheromones = np.ones((n_cities, n_cities))
visibility = 1 / (distances + 1e-10)  # avoid division by zero

def aco_tsp():
    best_cost = float('inf')
    best_solution = None
    
    for iteration in range(n_iterations):
        all_routes = []
        all_costs = []

        for ant in range(n_ants):
            start_city = 0 if ant < n_ants // 2 else 1
            tour = [start_city]
            current_city = start_city

            for _ in range(n_cities - 1):
                probabilities = (pheromones[current_city] ** alpha) * (visibility[current_city] ** beta)
                probabilities[tour] = 0  # set visited cities' probabilities to 0
                next_city = np.random.choice(range(n_cities), p=probabilities / probabilities.sum())
                tour.append(next_city)
                current_city = next_city

            # Returning to the starting depot
            tour.append(start_city)

            cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
            if cost < best_cost:
                best_cost = cost
                best_solution = tour

            all_routes.append(tour)
            all_costs.append(cost)

            # Update pheromones with this ant's solution
            for i in range(len(tour) - 1):
                pheromones[tour[i], tour[i + 1]] += pheromone_constant / cost
        
        # Evaporate pheromones
        pheromones *= (1 - pheromone_evaporation_rate)

    return best_solution, best_cost

tour, cost = aco_tsp()
print("Best Tour:", tour)
print("Total Travel Cost:", cost)