import random
import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# Step 1: Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52),
    2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69), 16: (38, 46), 
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Step 2: Calculate distance matrix between all cities
city_locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(city_locations, city_locations)

# Number of robots and depots
num_robots = 2
depots = [0, 1]  # Robot 0 starts at city 0, Robot 1 starts at city 1

# Step 3: Chromosome representation
# Chromosome is a permutation of cities excluding the depot cities and followed by a separator for dividing cities among robots
def initial_chromosome():
    cities_wo_depots = list(set(cities.keys()) - set(depots))
    random.shuffle(cities_wo_depots)
    separator = random.randint(1, len(cities_wo_depots)-1)  # Separator to split cities between the two robots
    return cities_wo_depots, separator

# Step 4: Fitness Function - Calculate total travel cost
def calculate_tour_cost(tour):
    cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return cost

def fitness(chromosome):
    cities_perm, separator = chromosome
    # Create tours based on separator
    tour1 = [0] + cities_perm[:separator] + [0]
    tour2 = [1] + cities_perm[separator:] + [1]
    
    cost1 = calculate_tour_cost(tour1)
    cost2 = calculate_tour_cost(tour2)
    return cost1 + cost2, tour1, cost1, tour2, cost2

# Simple genetic algorithm operations:
def crossover(ch1, ch2):
    cities_perm1, sep1 = ch1
    cities_perm2, sep2 = ch2
    point = random.randint(1, len(cities_perm1)-1)
    new_perm1 = list(cities_perm1[:point]) + list(cities_perm2[point:])
    new_perm2 = list(cities_perm2[:point]) + list(cities_perm1[point:])
    new_sep1 = random.randint(1, len(new_perm1)-1)
    new_sep2 = random.randint(1, len(new_perm2)-1)
    return (new_perm1, new_sep1), (new_perm2, new_sep2)

def mutate(chromosome, mutation_rate=0.1):
    cities_perm, separator = chromosome
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(cities_perm)), 2)
        cities_perm[idx1], cities_perm[idx2] = cities_perm[idx2], cities_perm[idx1]
        # Randomly adjust separator
        separator = random.randint(1, len(cities_perm)-1)
    return cities_perm, separator

# Genetic algorithm main loop
def run_genetic_algorithm(population_size=100, generations=300):
    # Initial population
    population = [initial_chromosome() for _ in range(population_size)]
    
    best_solution = None
    best_fitness = float('inf')
    
    for generation in range(generations):
        # Compute fitness for each individual
        population_fitness = []
        for ind in population:
            fit, _, _, _, _ = fitness(ind)
            population_fitness.append((fit, ind))
        
        # Selection of the best solution
        population_fitness.sort(key=lambda x: x[0])
        if population_fitness[0][0] < best_fitness:
            best_fitness, best_solution = population_fitness[0]
            print(f"Generation {generation}: Best Fitness = {best_fitness}")
        
        # Crossover and Mutation
        new_population = population_fitness[:2]  # Elitism: Keep the 2 best solutions
        while len(new_population) < population_size:
            # Parent selection and crossover
            p1, p2 = random.sample(population, 2)
            offspring1, offspring2 = crossover(p1, p2)
            # Mutate offsprings
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            new_population.extend([offspring1, offspring2])
        
        population = [x for _, x in new_population]
    
    return best_solution, best_fitness

# Execute genetic algorithm
best_chromosome, _ = run_genetic_algorithm()
total_fitness, tour1, cost1, tour2, cost2 = fitness(best_chromosome)

print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost1:.2f}")
print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost2:.2f}")
print(f"Overall Total Travel Cost: {total_fitness:.2f}")