import numpy as np
import random

# Given data: cities and their coordinates including depots
city_coords = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
])

def euclidean_distance(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Calculate distance matrix
n_cities = len(city_coords)
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i, j] = euclidean distance(city_coords[i], city_coords[j])

# Ant Colony Optimization specific parameters
n_ants = 20
n_iterations = 100
decay = 0.1
alpha = 1  # influence of pheromone on direction
beta = 5   # influence of heuristic value (inverse of distance)
pheromone = np.ones((n_cities, n_cities)) * 0.1  # initial pheromone level
visibility = 1 / (dist_matrix + 1.e-10)  # visibility (heuristic: 1/distance)

def aco_tsp(distances, n_depots=2):
    best_tour_length = np.inf
    best_tour = None

    for iteration in range(n_iterations):
        all_tours = []
        all_lengths = []
        
        for ant in range(n_ants):
            # Let ants start at one of the depots
            start = random.randint(0, n_depots-1)
            tour = [start]
            current = start
            
            for step in range(1, n_cities):
                # Select next city with probability influenced by pheromone and distance
                probabilities = pheromone[current] ** alpha * visibility[current] ** beta
                probabilities[tour] = 0  # set visited cities' probabilities to 0
                probabilities /= probabilities.sum()
                next_city = np.random.choice(n_cities, p=probabilities)
                tour.append(next_city)
                current = next_city

            # Complete tour by returning to depot
            tour.append(start)
            # Calculate tour length
            length = 0
            for i in range(1, len(tour)):
                length += distances[tour[i - 1], tour[i]]
            all_tours.append(tour)
            all_lengths.append(length)

            # Update best tour if found
            if length < best_tour_length:
                best_tour_length = length
                best_tour = tour

        # Update pheromone levels
        pheromone *= (1 - decay)  # pheromone evaporation
        for i, tour in enumerate(all_tours):
            for j in range(1, len(tour)):
                pheromone[tour[j - 1], tour[j]] += 1.0 / all_lengths[i]

    return best_tour, best_tour_length

# Solve the mTSP for 2 robots starting at 2 depots
best_tour, best_tour_length = aco_tsp(dist_matrix)
print("Best tour:", best_tour)
print("Best tour length:", best_tour_length)