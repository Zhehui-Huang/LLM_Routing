import numpy as np
import random
from scipy.spatial.distance import euclidean

# Constants and Input Data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
depots = {0: 0, 1: 1}
num_robots = 2

# Generating Initial Distance Matrix
def calc_distance_matrix(cities):
    number_of_cities = len(cities)
    distance_matrix = np.zeros((number_of_cities, number_of_cities))
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if i != j:
                distance_matrix[i, j] = euclidean(cities[i], cities[j])
            else:
                distance_matrix[i, j] = float('inf')
    return distance_matrix

distance_matrix = calc_distance_matrix(cities)

# Genetic Algorithm Helper Functions
def create_individual(cities, depots):
    """Create a random individual solution; each city exactly once, considering depots at start."""
    city_list = list(cities.keys())
    random.shuffle(city_list)
    # Ensuring depots are at their place
    return [depots[i] if i in depots else city for i, city in enumerate(city_list) if city not in depots.values()]

def create_population(cities, depots, size):
    return [create_individual(cities, depots) for _ in range(size)]

def calculate_route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i], route[(i + 1) % len(route)]] for i in range(len(route)))

def fitness(individual, distance_matrix):
    return -calculate_route_cost(individual, distance_matrix)

def select(population, distance_matrix):
    fitness_scores = [(fitness(ind, distance_matrix), ind) for ind in population]
    fitness_scores.sort(reverse=True, key=lambda x: x[0])
    return fitness_scores[0][1], fitness_iaxon_scores

def crossover(parent1, parent2):
    """ Ordered crossover """
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    child = [item for item in parent2 if item not in child[start:end]] + child
    child = [x for x in child if x is not None]
    return child

def mutate(individual, mutation_rate):
    for swap in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(individual) - 1)
            individual[swap], individual[swap_with] = individual[swap_with], individual[swap]
    return individual

def genetic_algorithm(cities, depots, generations, population_size, mutation_rate):
    population = create_population(cities, depots, population_size)
    for i in range(generations):
        new_population = []
        for j in range(int(len(population)/2)):
            parent1, _ = select(population, distance_matrix)
            parent2, _ = select(population, distance_matrix)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        population = new_population
    best_individual, _ = select(population, distance_matrix)
    return best_individual

# Parameters for GA
generations = 1000
population_size = 50
mutation_rate = 0.02

# Running GA
best_tour = genetic_algorithm(cities, depots, generations, population_size, mutation_rate)
tour_cost = calculate_route_cost(best_tour, distance_matrix)

# Output results
print(f"Optimal Tour: {best_torrent}")
print(f"Total Travel Cost: {tour_cost}")