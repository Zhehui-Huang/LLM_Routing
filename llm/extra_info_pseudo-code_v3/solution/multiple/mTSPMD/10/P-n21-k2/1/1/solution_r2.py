import numpy as np
from scipy.spatial.distance import euclidean
import random

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to compute the distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Genetic Algorithm Implementation
def initial_population(depot_indices, num_individuals=50):
    cities = list(range(len(coordinates)))
    for depot in depot_indices:
        cities.remove(depot)
    population = []
    for _ in range(num_individuals):
        random.shuffle(cities)
        split = round(len(cities) / 2)
        population.append([depot_indices[0]] + cities[:split] + [depot_indices[0]])
        population.append([depot_indices[1]] + cities[split:] + [depot_indices[1]])
    return population

# Calculate cost
def tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Genetic operators
def crossover(parent1, parent2, depot):
    mid = len(parent1) // 2
    child = [depot] + random.sample(parent1[1:-1]+parent2[1:-1], len(parent1)-2) + [depot]
    return child

def mutate(tour, mutation_rate=0.1):
    for i in range(1, len(tour)-1):
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour)-2)
            tour[i], tour[j] = tour[j], tour[i]
    return tour

# Main GA procedure
def genetic_algorithm(depot_indices, generations=100, pop_size=50):
    population = initial_population(depot_indices, pop_size)
    for _ in range(generations):
        new_pop = []
        costs = sorted([(indiv, tour_cost(indiv)) for indiv in population], key=lambda x: x[1])
        for parent1, parent2 in zip(costs[::2], costs[1::2]):
            child1 = crossover(parent1[0], parent2[0], parent1[0][0])
            child2 = crossover(parent2[0], parent1[0], parent2[0][0])
            new_pop.extend([mutate(child1), mutate(child2)])
        population = new_pop[:pop_size]

    # Final evaluation
    sorted_final_pop = sorted([(indiv, tour_cost(indiv)) for indiv in population], key=lambda x: x[1])
    robot_0_tour, cost_0 = [x for x in sorted_final_pop if x[0][0] == depot_indices[0]][0]
    robot_1_tour, cost_1 = [x for x in sorted_final_pop if x[0][0] == depot_indices[1]][0]

    print(f"Robot 0 Tour: {robot_0_tour}")
    print(f"Robot 0 Total Travel Cost: {cost_0}")
    print(f"Robot 1 Tour: {robot_1_tour}")
    print(f"Robot 1 Total Travel Cost: {cost_1}")
    print(f"Overall Total Travel Cost: {cost_0 + cost_1}")

# Run the genetic algorithm
genetic_algorithm([0, 1])