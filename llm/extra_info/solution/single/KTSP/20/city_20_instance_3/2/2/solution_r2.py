import math
import random

# Cities coordinates dictionary
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create initial pool of cities to select from (excluding depot city 0 initially for permutations)
initial_cities = [i for i in range(1, 20)]
random.shuffle(initial_cities)
initial_cities = [0] + initial_cities[:12] + [0]  # start and end at depot

# Calculates the total cost of a given tour
def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Genetic algorithm configuration
population_size = 100
generations = 1000
mutation_rate = 0.05

# Generate initial population
def generate_initial_population(size, initial):
    population = []
    for _ in range(size):
        new_tour = initial[1:-1]
        random.shuffle(new_tour)
        population.append([initial[0]] + new_tour + [initial[0]])
    return population

# Tournament selection
def tournament_selection(pop, k=3):
    best = random.choice(pop)
    for _ in range(k-1):
        indiv = random.choice(pop)
        if calculate_cost(indiv) < calculate_cost(best):
            best = indiv
    return best

# Crossover
def ordered_crossover(parent1, parent2):
    size = len(parent1)
    a, b = sorted(random.sample(range(1, size-1), 2))
    child = [None]*size
    child[a:b] = parent1[a:b]
    fill = [item for item in parent2 if item not in child]
    fill_pointer = 0
    for i in range(size):
        if not child[i]:
            child[i] = fill[fill_pointer]
            fill_pointer += 1
    return child

# Mutation - Swap two cities
def mutate(tour):
    if random.random() < mutation_rate:
        a, b = sorted(random.sample(range(1, len(tour)-1), 2))
        tour[a], tour[b] = tour[b], tour[a]
    return tour

# Genetic algorithm main loop
population = generate_initial_population(population_size, initial_cities)
for _ in range(generations):
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_two_point(population)
        child = ordered_crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population

# Find the best solution 
best_tour = min(population, key=calculate_cost)
best_cost = calculate_cost(best_tour)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)