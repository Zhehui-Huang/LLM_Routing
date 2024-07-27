import numpy as for np
import random

# Define city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Compute Euclidean distance between cities
def euclidean_distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Prepare distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_memory_matrix[i][j] = euclidean_distance(i, j)

# Ant Colony Optimization parameters
num_ants = 20
num_iterations = 100
alpha = 1
beta = 5
evaporation_rate = 0.5
pheromone_deposit = 10
initial_pheromone = 1.0 / num_cities
pheromone_matrix = initial_pheromone * np.ones((num_cities, num_cities))

# ACO algorithm function
def aco_tsp(depot_start):
    best_tour = None
    best_cost = float('inf')
    
    for iteration in range(num_iterations):
        for ant in range(num_ants):
            tour = [depot_start]
            current_city = depot_start
            while len(tour) < num_cities:
                next_city = select_next_city(current_city, tour)
                tour.append(next_city)
                current_city = next_city
            tour.append(depot_start)  # return to starting depot
            cost = calculate_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour[:]
            deposit_pheromone(tour, cost)
        evaporate_pheromone()
    return best_tour, best_cost

def select_next_city(current_city, tour):
    probabilities = []
    for city in range(num_cities):
        if city not in tour:
            heuristic = 1 / (distance_matrix[current_city][city] + 1e-5)
            probability = (pheromone[current_city][city] ** alpha) * (heuristic ** beta)
            probabilities.append(probability)
        else:
            probabilities.append(0)
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    return np.random.choice(num_cities, p=probabilities)

def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def deposit_pheromone(tour, cost):
    for i in range(len(tour) - 1):
        pheromone_matrix[tour[i]][tour[i + 1]] += pheromone_deposit / cost

def evaporate_pheromone():
    pheromone_matrix *= (1 - evaporation_rate)

# Solve for robots starting at their respective depots
results = []
for depot in [0, 1]:
    tour, cost = aco_tsp(depot)
    results.append((tour, cost))

# Printing results
overall_total_cost = 0
for i, (tour, cost) in enumerate(results):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    overall_total_cost += cost

print(f"Overall Total Travel Cost: {overall_total_cost}")