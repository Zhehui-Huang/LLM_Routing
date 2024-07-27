import random
from math import sqrt

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial population
def generate_tour():
    tour = list(range(1, 15))  # City indices except depot
    random.shuffle(tour)
    tour = [0] + tour[:11] + [0]   # Select 11 cities randomly + depot as start and end
    return tour

# Fitness function (Total distance of tour)
def calculate_fitness(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Genetic Algorithm Settings
population_size = 100
generations = 500
mutation_rate = 0.1
population = [generate_tour() for _ in range(population_size)]

# Evolution
for generation in range(generations):
    # Compute fitness for each individual
    fitness_scores = [(calculate_fitness(individual), individual) for individual in population]
    fitness_scores.sort()
    
    # Select the best performing individuals
    survivors = fitness_scores[:population_size // 2]
    population = [ind for _, ind in survivors]
    
    # Create next generation
    while len(population) < population_size:
        if random.random() < 0.7:  # Crossover
            parent1 = random.choice(survivors)[1]
            parent2 = random.choice(survivors)[1]
            cut = random.randint(1, len(parent1) - 2)
            child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
            population.append(child)
        
        # Mutation
        if random.random() < mutation_rate:
            mutate_idx = random.randint(1, len(child) - 2)
            swap_with = random.randint(1, len(child) - 2)
            child[mutate_idx], child[swap_with] = child[swap_with], child[mutate_idx]
    
    # Report best result of this generation
    best_distance, best_tour = fitness_scores[0]
    if generation == generations - 1:
        print(f"Tour: {best_tour}")
        print(f"Total travel cost: {best_distance:.2f}")

# Since it is very important, consider increasing generations or population size, or improving selection and mutation strategies.