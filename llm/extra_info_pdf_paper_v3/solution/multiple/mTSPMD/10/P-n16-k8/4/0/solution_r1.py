import numpy as np
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
    """Calculate the total distance of the mTSP solution based on individual robot tours."""
    total_cost = 0
    tours = {depot: [depot] for depot in depot_starts}

    index = 0
    # Distribute cities in the solution to each depot based on segment
    for depot in depot_starts:
        if index < len(solution):
            tours[depot].extend(solution[index:index+1])
            index += 1
        tours[depot].append(depot)  # Add return to the start point

    # Calculate tour cost for each depot
    for tour in tours.values():
        for i in range(len(tour) - 1):
            total_cost += distances[tour[i]][tour[i+1]]

    return total_cost, tours

# Genetic operations and algorithm definition below would follow similar structure,
# modified to be accurate with the above fixed fitness function.

def genetic_algorithm(cities, depots, num_generations=100, pop_size=50):
    non_depot_cities = [i for i in range(len(cities)) if i not in depots]
    population = [random.sample(non_depot_cities, len(non_depot_cities)) for _ in range(pop_size)]
    best_solution = None
    best_fitness = float('inf')

    for _ in range(num_generations):
        new_population = []
        # Select, crossover and mutate:
        for _ in range(pop_size):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        # Evaluate and select the best solution
        population = new_population
        for individual in population:
            cost, tours = fitness(individual, depots)
            if cost < best_fitness:
                best_fitness = cost
                best_solution = individual

    # Compute detail tour information for the best solution
    final_cost, final_tours = fitness(best_solution, depots)

    return final_tours, final_cost

# Running the genetic algorithm
final_tours, final_cost = genetic_algorithm(cities, depots)
for i, (depot, tour) in enumerate(final_tours.items()):
    tour_cost = sum(distances[tour[j]][tour[j+1]] for j in range(len(tour)-1))
    print(f"Robot {i} (Depot {depot}) Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_effective_cost}")

print(f"Overall Total Travel Cost: {final_cost}")