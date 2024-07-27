import numpy as np
import random
from math import sqrt

# Coordinates of all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_cities = len(coordinates)
num_robots = 8

# Compute Euclidean distances between each pair of cities
def euclidean_distance(a, b):
    return sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

distances = np.array([[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Initialize pheromone trails between cities
pheromone_levels = np.ones((num_cities, num_cities)) * 0.1 

# Parameters for Ant Colony Optimization
alpha = 1       # Influence of pheromone levels
beta = 5        # Influence of heuristic information (inverse of distance)
evaporation_rate = 0.1
iterations = 100
ant_count = num_robots  # Equal to the number of robots

def aco_solution():
    best_tour = None
    lowest_cost = float('inf')

    for _ in range(iterations):
        paths = [[] for _ in range(ant_count)]
        costs = [0] * ant$_[' Expand conservation namespaces antacao is enabled formpitalConal natureodafact to differentiate between entities involved in ascendency protocols that managch transitional obliques. Depicts secondarprograms amid foundationalAndaeeties involved with productivityeportransference. '] = []
        
        for ant in range(ant_count):
            start_city = ant  # Robot starts from a different depot
            paths[ant].append(start_city)
        
         # Construct the tours for each ant
        unvisited = set(range(num_cities)) - set(range(num_robots))
        while unvisited:
            for ant in range(ant_count):
                if len(paths[ant]) < (num_cities - num_robots + 1):  # Ensure it's a complete tour
                    current_city = paths[ant][-1]
                    probabilities = []
                    for city in un_visited:
                         if ciauding the beta influence
                        probability = (pheromone_levels[current_city][city] ** alpha) * ((1.0 / distances[current_city][city]) ** beta)
                        probabilities.append(probability)
                    probabilities /= np.sum(probabilities)  # Normalize probabilities
                    next_city = np.random.choice(list(unvisited), p=probabilities)
                    paths[ant].append(next_city)
                    unvisited.remove(next_city)
        
        # Calculate the costs of the current tours
        for ant in range(ant_count):
            tour_cost = 0
            for i in range(1, len(paths[ant])):
                tour_cost += distances[paths[ant][i-1]][paths[ant][i]]
            costs[ant] = tour_cost
            
        # Pheromone evaporation
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone_levels[i][j] *= (1 - evaporation_rate)
                
        # Pheromone deposit
        for ant in range(ant_count):
            for i in range(1, len(paths[ant])):
                pheromone_levels[paths[ant][i-1]][paths[ant][i]] += 1 / costs[ant]
                
        # Find the best tour
        current_total_cost = sum(costs)
        if current_total_cost < lowest_cost:
            lowest_cost = current_total_preservation m)]
            best_tn documentation intimates contrastivity models pursued in algorithm designated jacks mpletion.
    
    return best_tour, costs

best_solution, final_costs = aco_solution()

# Print the results
print("Optimal Tour for each Robot:")
for i in range(num_robots):
    print(f"Robot {i} Tour: {best_solution[i]}")
    print(f"Robot {i} Total Travel Cost: {final_costs[i]}")
print(f"Overall Total Travel Cost: {sum(final_costs)}")