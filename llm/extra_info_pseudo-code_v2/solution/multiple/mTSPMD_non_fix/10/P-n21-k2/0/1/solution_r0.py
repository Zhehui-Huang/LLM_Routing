import random
import math

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Euclidean distance calculator
def distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initialize GA parameters
num_generation = 100
population_size = 20
mutation_rate = 0.15
crossover_rate = 0.7

# Generate initial population: list of tuples (chromosome, fitness)
def create_initial_population():
    population = []
    all_cities = list(cities.keys())[2:]  # excluding depots
    for _ in range(population_size):
        random.shuffle(all_cities)
        # Create a simple round trip starting and ending at depot 0
        chromosome = [0] + all_cities + [1]  # depot 0 -> cities -> depot 1
        fitness = calculate_fitness(chromosome)
        population.append((chromosome, fitness))
    return population

# Calculate total distance for a given chromosome path
def calculate_fitness(chromosome):
    total_dist = 0
    for i in range(1, len(chromosome)):
        total_dist += distance(chromosome[i-1], chromosome[i])
    return total_dist

# Parent selection via tournament selection
def select_parents(population):
    best = None
    for _ in range(2):  # binary tournament
        ind = random.choice(population)
        if best is None or ind[1] < best[1]:
            best = ind
    return best

# Perform crossover (here using a simple one-point crossover)
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1, parent2
    cut = random.randint(1, len(parent1) - 2)
    child1 = parent1[:cut] + parent2[cut:]
    child2 = parent2[:cut] + parent1[cut:]
    return child1, child2

# Mutation operator for an individual chromosome (simple swap mutation)
def mutate(chromosome):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(chromosome) - 1), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Genetic algorithm process
def genetic_algorithm():
    population = create_initial_population()
    
    for generation in range(num_generation):
        new_population = []
        while len(new_population) < population_size:
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            child1, child2 = crossover(parent1[0], parent2[0])
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append((child1, calculate_fitness(child1)))
            new_population.append((child2, calculate_fitness(child2)))
        population = sorted(new_population, key=lambda x: x[1])[:population_size]
    
    best_solution = min(population, key=lambda x: x[1])
    return best_solution

# Run the genetic algorithm and print results
best_chromosome, best_fitness = genetic_algorithm()
print("Best tour:", best_chromosome)
print("Best total travel cost:", best_fitness)