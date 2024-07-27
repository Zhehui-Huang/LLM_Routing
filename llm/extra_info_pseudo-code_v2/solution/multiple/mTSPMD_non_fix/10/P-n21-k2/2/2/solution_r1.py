import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define city coordinates
cities = [ 
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_cities = len(cities)  # Total cities
num_depots = 2  # Cities with indices 0 and 1 are depots
num_robots = 2

# Helper function to calculate Euclidean distance between cities
def distance(city1, city2):
    return euclidean(city1, city2)

# Generates an individual route
def generate_individual():
    path = list(range(num_depots, num_cities))  # Create a list of cities excluding depots
    random.shuffle(path)
    return [0] + path + [1]  # Start at depot 0, end at depot 1

# Population initialization
def initialize_population(size):
    return [generate_individual() for _ in range(size)]

# Fitness function: Calculate total distance traveled for the chromosome
def calculate_fitness(individual):
    total_dist = 0
    for i in range(len(individual) - 1):
        total_dist += distance(cities[individual[i]], cities[individual[i+1]])
    return total_dist

# Selection process
def tournament_selection(pop, k=3):
    best = random.choice(pop)
    for _ in range(k - 1):
        indiv = random.choice(pop)
        if calculate_fitness(indiv) < calculate_fitness(best):
            best = indiv
    return best

# Crossover operator
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, num_cities - 1), 2))  # Avoiding depots
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    child[0], child[-1] = 0, 1  # Fixing depots
    fill = (gene for gene in parent2 if gene not in parent1[start:end+1] and gene not in [0, 1])
    for i in range(len(child)):
        if child[i] is None:
            child[i] = next(fill)
    return child

# Mutation operator
def mutate(individual, mutation_rate=0.01):
    for i in range(1, num_cities - 1):  # Avoiding depots
        if random.random() < mutation_rate:
            j = random.randint(1, num_cities - 2)
            individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm implementation
def genetic_algorithm(pop_size=100, generations=500):
    pop = initialize_population(pop_size)
    
    for _ in range(generations):
        new_pop = []
        while len(new_pop) < pop_size:
            parent1 = tournament_selection(pop)
            parent2 = tournament_selection(pop)
            if random.random() < 0.8:  # Crossover rate
                child = crossover(parent1, parent2)
            else:
                child = parent1
            child = mutate(child)
            new_pop.append(child)
        pop = new_pop
    
    # Find the best solution
    best_solution = min(pop, key=calculate_fitness)
    return best_solution


# Run GA
best_route = genetic_algorithm(100, 300)
best_cost = calculate_fitness(best_route)

print("Best route found:", best_route)
print("Total distance:", best_cost)