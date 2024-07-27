import numpy as  np
from scipy.spatial.distance import euclidean
from random import sample, randint, random
import heapq

# City coordinates
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

# Calculate distances matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for from_idx in cities:
        for to_idx in cities:
            if from_idx != to_idx:
                distances[from_idx, to_idx] = euclidean(cities[from_idx], cities[to_idx])
            else:
                distances[from_idx, to_idx] = float('inf')  # Infinite cost to self-loop
    return distances

distances = calculate_distances(cities)

# Genetic algorithm parameters
num_generations = 5000
population_size = 100
mutation_rate = 0.1
num_cities = len(cities)
num_robots = 2
elite_size = int(0.2 * population_size)

# Create a random individual
def create_individual():
    tour = list(range(2, num_cities)) # Excluding depots
    sample_tour = sample(tour, len(tour))
    # Random split point for two robots
    split = randint(1, len(sample_tour) - 1)
    return sample_tour[:split], sample_tour[split:]

# Calculate cost of the tour
def calculate_cost(tour, depot):
    tour_cost = distances[depot, tour[0]]
    for i in range(1, len(tour)):
        tour_cost += distances[tour[i-1], tour[i]]
    tour_cost += distances[tour[-1], depot]
    return tour_cost

# Evaluate fitness of the population
def fitness(individual):
    tour1, tour2 = individual
    cost1 = calculate_cost(tour1, 0)
    cost2 = calculate_cost(tour2, 1)
    return 1 / (cost1 + cost2), cost1, cost2

# Select parents using tournament selection
def tournament_selection(population, k=3):
    return min(sample(population, k), key=lambda ind: fitness(ind)[0])

# Perform crossover between two parents
def ordered_crossover(parent1, parent2):
    child1, child2 = [], []
    # Choose crossover points
    cut1, cut2 = sorted(sample(range(num_cities-2), 2))
    child1_gap = [gene for gene in parent2[0] if gene not in parent1[0][cut1:cut2+1]]
    child2_gap = [gene for gene in parent1[0] if gene not in parent2[0][cut1:cut2+1]]
    
    # Create the child
    child1 = child1_gap[:cut1] + parent1[0][cut1:cut2+1] + child1_gap[cut1:]
    child2 = child2_gap[:cut1] + parent2[0][cut1:cut2+1] + child2_gap[cut1:]
    return (child1, child2), split

# Mutate an individual by swapping two cities
def mutate(individual):
    tour1, tour2 = individual
    if random() < mutation_rate:
        idx1, idx2 = sample(range(len(tour1)), 2)
        tour1[idx1], tour1[idx2] = tour1[idx2], tour1[idx1]
    if random() < mutation_rate:
        idx1, idx2 = sample(range(len(tour2)), 2)
        tour2[idx1], tour2[idx2] = tour2[idx2], tour2[idx1]
    return tour1, tour2

# Create initial population
population = [create_individual() for _ in range(population_size)]

# Evolutionary loop
for generation in range(num_generations):
    # Evaluate the population
    pop_with_fit = sorted([(ind, fitness(ind)) for ind in population], key=lambda x: x[1][0])

    # Elitism
    new_population = [x[0] for x in pop_with_fit[:elite_size]]

    # Generate new offsprings
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child, _ = ordered_crossover(parent1, parent2)
        new_population.append(mutate(child))
    
    population = new_population
    if generation % 500 == 0:
        print(f"Generation {generation}: Best fitness = {pop_with_fit[0][1]}")

best_solution = pop_with_fit[0]
tour1, tour2 = best_solution[0]
cost1, cost2 = best_solution[1][1], best_solution[1][2]

print("Robot 0 Tour:", [0] + tour1 + [0])
print("Robot 0 Total Travel Cost:", cost1)
print("Robot 1 Tour:", [1] + tour2 + [1])
print("Robot 1 Total Travel Cost:", cost2)
print("Overall Total Travel Cost:", cost1 + cost2)