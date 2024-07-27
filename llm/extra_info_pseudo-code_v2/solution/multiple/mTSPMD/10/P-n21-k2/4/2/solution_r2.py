import numpy as np
import random

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.hypot(city1[0] - city2[0], city1[1] - city2[1])

# City coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Parameters for ACO
num_ants = 10
num_iterations = 100
alpha = 1.0  # Pheromone importance
beta = 2.0   # Distance priority
evaporation_rate = 0.5
pheromone_deposit = 1.0
initial_pheromone = 0.1

# Number of cities
num_cities = len(cities_coordinates)

# Distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Pheromone matrix
pheromone_matrix = np.ones((num_cities, num_cities)) * initial_pheromone

# Ant Colony Optimization function
def ant_colony_optimization():
    best_route = None
    best_distance = float('inf')

    for iteration in range(num_iterations):
        routes = []
        distances = []

        for ant in range(num_ants):
            route = random.sample(range(num_cities), num_cities)
            route.append(route[0])  # To make it a round trip
            total_distance = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

            if total_distance < best_distance:
                best_distance = total_distance
                best_route = route

            routes.append(route)
            distances.append(total_distance)

        # Pheromone evaporation
        pheromone_matrix *= (1 - evaporation_rate)
        
        # Pheromone depositing
        for i in range(num_ants):
            deposit_amount = pheromone_deposit / distances[i]
            for j in range(num_cities):
                pheromone_matrix[routes[i][j], routes[i][j+1]] += deposit_amount
                # Since it's a symmetric TSP
                pheromone_matrix[routes[i][j+1], routes[i][j]] += deposit_amount

    return best_route, best_distance

# Running the optimization
best_route, best_distance = ant_colony_optimization()

# Map route indexes to depots and cities
best_route_mapped = best_route.copy()  # This maps indexes directly to city numbers as initially provided.

# Output results
print(f"Best Route: {best_route_mapped}")
print(f"Best Distance (Cost): {best_distance:.2f}")