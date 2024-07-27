import numpy as as np
import random
from math import sqrt

# Coordinates of cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of robots and their starting-ending depots
num_robots = 8
depots = list(range(num_robots))  # Depots are first 8 cities

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Pairwise distance matrix
distances = [
    [euclidean_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

def fitness(solution, depot_starts):
    """Calculate the total distance of the mTSP solution."""
    total_cost = 0
    tours = []

    # Decoding solution based on robot's assigned depot
    for depot in depot_starts:
        tour = [depot]
        for city in solution:
            if city not in tours and city not in depots:
                tour.append(city)
        tour.append(depot)
        tours.append(tour)

        # Calculate tour cost
        tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += tour_cost

    return total_cost, tours

# Initialize population
def initialize_population(pop_size, non_depot_cities):
    """Create an initial population of solutions."""
    population = []
    for _ in range(pop_size):
        individual = non_depot_cities[:]
        random.shuffle(individual)
        population.append(individual)
    return population

# Genetic operators
def crossover(parent1, parent2):
    """Perform a crossover operation and return a new offspring."""
    idx1, idx2 = sorted(random.sample(range(len(parent1)), 2))
    offspring = [None]*len(parent1)
    offspring[idx1:idx2+1] = parent1[idx1:idx2+1]
    fill_values = [x for x in parent2 if x not in offspring]
    idx_fill = 0
    for i in range(len(offspring)):
        if offspring[i] is None:
            offspring[i] = fill_values[idx_fill]
            idx_fill += 1
    return offspring

def mutate(individual, mutation_rate=0.1):
    """Perform mutation on an individual."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            # Swap mutation
            individual[i], individual[j] = individual[j], individual[i]

# Main genetic algorithm
def genetic_algorithm(cities, depots, num_generations=1000, pop_size=100):
    non_depot_cities = [city for city in range(len(cities)) if city not in depots]
    population = initialize_population(pop_size, non_depot_cities)
    best_solution = None
    best_fitness = float('inf')

    for _ in range(num_generations):
        new_population = []
        while len(new_population) < pop_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            offspring = crossover(parent1, parent2)
            mutate(offspring)
            new_population.append(offspring)

        # Evaluate population
        for individual in new_population:
            cost, _ = fitness(individual, depots)
            if cost < best_fitness:
                best_fitness = cost
                best_solution = individual

        population = new_population

    total_cost, tours = fitness(best_solution, depots)
    return tours, total_cost

# Run the GA
tours, total_cost = genetic_algorithm(cities, depots)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    tour_cost = sum(distances[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")