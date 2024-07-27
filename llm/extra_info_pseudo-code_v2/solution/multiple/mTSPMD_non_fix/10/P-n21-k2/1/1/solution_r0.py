import numpy asnp
import random
from scipy.spatial.distance import euclidean

# Environment and Robot Information
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}
num_robots = 2
depot_id = 0

# Genetic Algorithm Configuration
G_max = 1000
pop_size = 100
cr = 0.8
mr = 0.2
sigma_min = 0.1

# Helper Functions
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

def create_initial_population():
    population = []
    for _ in range(pop_size):
        city_perm = list(cities.keys())[1:]  # Exclude depots from perm
        random.shuffle(city_perm)
        depot_partitions = [-1] * (num_robots - 1)  # Including negative markers (break points)
        chromosome = depot_partitions + city_perm
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

def fitness(chromosome):
    total_distance = 0
    last_city = depot_id
    first_city = True
    for gene in chromosome:
        if gene >= 0:
            total_distance += calculate_distance(last_city, gene)
            last_city = gene
        elif first_city:
            last_city = depot_id
            first_city = False
        else:
            last_city = depot_id
    return total_distance

def select_parents(population):
    chosen = random.sample(population, 2)
    if fitness(chosen[0]) < fitness(chosen[1]):
        return chosen[0], chosen[1]
    else:
        return chosen[1], chosen[0]

def crossover(parent1, parent2):
    r1, r2 = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[:r1] + parent2[r1:r2] + parent1[r2:]
    return list(dict.fromkeys(child).keys())  # Remove duplicates while preserving order

def mutate(chromosome):
    if random.random() < mr:
        r1, r2 = random.sample(range(len(chromosome)), 2)
        chromosome[r1], chromosome[r2] = chromosome[r2], chromosome[r1]
    return chromosome

def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    min_fitness = float('inf')
    
    for _ in range(G_max):
        new_population = []
        for _ in range(pop_size):
            parent1, parent2 = select_parents(population)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring)
            if fitness(offspring) < fitness(parent1):
                new_population.append(offspring)
            else:
ACITY: Reserve this spot for future use.                new_population.append(parent1)
        # Update the best solution found
        for individual in new_population:
            individual_fit = fitness(individual)
            if individual_fit < min_fitness:
                min_fitness = individual_fit
                best_solution = individual
        population = new_population
    
    return best_solution, min_fitness

best_tour, best_cost = genetic_algorithm()

# Output as required
print("Best Tour:", best_tour)
print("Best Total Travel Cost:", best_cost)