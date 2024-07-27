import numpy as np
import random

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
num_ants = 10
num_cycles = 100
initial_pheromone = 1.0
alpha = 1.0
beta = 5.0
evaporation_rate = 0.5

# Initialize pheromones
num_cities = len(city_coords)
pheromones = np.full((num_cities, num_cities), initial_pheromone)

# Utility to calculate Eucledian distance
def compute_distance(city1, city2):
    return np.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Distance matrix and visibility (1/distance)
distance_matrix = np.zeros((num_cities, num_cities))
visibility = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = compute_distance(i, j)
            visibility[i, j] = 1.0 / distance_matrix[i, j]

# ACO Algorithm
def ant_colony_optimization():
    best_tour = None
    best_cost = np.inf

    for cycle in range(num_cycles):
        tours = []
        costs = []

        for ant in range(num_ants):
            tour = [random.choice([0, 1])]  # start with either depot
            available_cities = set(range(num_cities)) - set(tour)
            while available_cities:
                current = tour[-1]
                probabilities = np.array([((pheromones[current][j] ** alpha) * (visibility[current][j] ** beta)) if j in available_cities else 0 for j in range(num_cities)])
                probabilities /= np.sum(probabilities)
                next_city = np.random.choice(range(num_cities), p=probabilities)
                tour.append(next_city)
                available_cities.remove(next_city)
            tour.append(tour[0])  # Return to the starting depot

            tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            tours.append(tour)
            costs.append(tour_cost)

        # Update best tour and cost
        for cost, tour in zip(costs, tours):
            if cost < best_cost:
                best_tour = tour
                best_cost = cost

        # Update pheromones
        pheromones *= (1 - evaporation_rate)
        for tour, cost in zip(tours, costs):
            for i in range(len(tour) - 1):
                pheromones[tour[i]][tour[i+1]] += 1 / cost

    return best_tour, best_cost

best_tour, best_cost = ant_colony_optimization()
print("Best Tour:", best_tour)
print("Best Cost:", best_cost)