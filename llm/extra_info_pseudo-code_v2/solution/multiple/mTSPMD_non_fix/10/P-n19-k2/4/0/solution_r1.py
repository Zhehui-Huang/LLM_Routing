import numpy as np
import random
from scipy.spatial.distance import euclidean

# Coordinates of cities
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Compute distance matrix
distance_matrix = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i, j] = euclidean(cities[i], cities[j])

# Genetic Algorithm Parameters
population_size = 50
num_generations = 1000
mutation_rate = 0.15
elite_size = 0.2

# Helpers and Genetic Operators

def create_individual():
    """Create a route beginning at 0 and assigning all city indices except for depot 0 and 1."""
    route = list(range(2, len(cities)))  # start from city 2
    random.shuffle(route)
    return [0] + route  # start at depot 0

def calculate_cost(route):
    """Calculate the total distance of a route."""
    return sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))

def crossover(parent1, parent2):
    """Ordered crossover."""
    start, end = sorted(random.sample(range(1, len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end] = parent1[start:end]
    pointer = 0
    for item in parent2:
        if item not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = item
    return child

def mutate(individual, rate):
    """Swap mutation."""
    for i in range(1, len(individual)):
        if random.random() < rate:
            j = random.randint(1, len(individual)-1)
            individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    # Initial population
    population = [create_individual() for _ in range(population_size)]

    # Evolution
    for generation in range(num_generations):
        # Evaluate fitness
        fitness_scores = [calculate_cost(ind) for ind in population]
        
        # Selection based on fitness
        sorted_indices = np.argsort(fitness_scores)
        population = [population[i] for i in sorted_indices]
        
        # Keep the best
        num_elites = int(elite_size * population_size)
        next_generation = population[:num_elites]
        
        # Crossover and mutation to generate new solutions
        while len(next_generation) < population_size:
            parent1, parent2 = random.choices(population[:num_elites], k=2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_generation.append(child)
        
        population = next_generation

    # Best solution
    best_route = min(population, key=calculate_cost)
    return best_route

# Run Genetic Algorithm
best_route = genetic_algorithm()
best_route.append(1)  # Indicate end at depot 1
tour_cost = calculate_cost(best_route)

print(f"Robot 0 Tour: {best_route}")
print(f"Robot 0 Total Travel Cost: {tour_cost:.2f}")