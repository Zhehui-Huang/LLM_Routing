import math
import random

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Distance between cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create matrix of distances between cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def total_and_max_distance(route):
    total_dist = 0
    max_dist = 0
    for i in range(1, len(route)):
        dist = distances[route[i-1]][route[i]]
        total_dist += dist
        if dist > max_dist:
            max_dist = dist
    return total_dist, max_dist

# Generate initial population of routes
def create_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        perm = list(range(1, num_cities))
        random.shuffle(perm)
        population.append([0] + perm + [0])
    return population

# Genetic algorithm operations
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    missing = [item for item in parent1 if item not in child]
    pointer = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = missing[pointer]
            pointer += 1
    return child

def mutate(route, mutation_rate):
    if random.random() < mutation_date:
        i, j = random.randint(1, len(route) - 2), random.randint(1, len(route) - 2)
        route[i], route[j] = route[j], route[i]

def select(population):
    weights = [1 / total_and_max_distance(route)[1] for route in population]
    total_weight = sum(weights)
    probabilities = [weight / total_weight for weight in weights]
    chosen_index = random.choices(range(len(population)), weights=probabilities, k=1)[0]
    return population[chosen_index]

# Main genetic algorithm function
def genetic_algorithm(pop_size, num_cities, num_generations, mutation_rate):
    population = create_initial_population(pop_size, num_cities)
    for _ in range(num_generations):
        new_population = []
        for _ in range(len(population)):
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_route = min(population, key=lambda x: total_and_max_distance(x)[1])
    total_dist, max_dist = total_and_max_distance(best_route)
    return best_route, total_dist, max_dist

# Parameters
population_size = 100
generations = 5000  # Increased number of generations for potentially better results
mutation_rate = 0.03  # Slightly decreased mutation rate

# Run the algorithm
best_route, total_cost, max_consecutive_distance = genetic_algorithm(population_size, len(cities), generations, mutation_rate)

# Output results
print("Tour:", best_route)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))