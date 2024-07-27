import numpy as np
import random

# Helper functions
def calc_distance(point1, point2):
    """Calculate Euclidean distance."""
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Create a matrix of distances
city_coords = [cities[i] for i in range(len(cities))]
distance_matrix = np.array([[calc_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))] for i in range(len(city_coords))])

def fitness(tour):
    """Return the fitness of a tour, inverse of the route's maximum edge length."""
    max_edge_length = max([distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1)])
    return 1.0 / max_edge_length, sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def create_tour():
    """Create a valid tour by shuffling the city indices."""
    tour = list(range(1, len(city_coords)))
    random.shuffle(tour)
    return [0] + tour + [0]

def crossover(tour1, tour2):
    """Perform ordered crossover."""
    start, end = sorted(random.sample(range(1, len(tour1) - 1), 2))
    child = [None]*len(tour1)
    child[start:end+1] = tour1[start:end+1]
    child_pointer = (end + 1) % len(tour1)
    parent_pointer = child_pointer
    while None in child:
        if tour2[parent_pointer] not in child:
            child[child_pointer] = tour2[parent_pointer]
            child_pointer = (child_pointer + 1) % len(tour1)
        parent_pointer = (parent_pointer + 1) % len(tour1)
    return child

def mutate(tour, mutation_rate=0.1):
    """Perform swap mutation."""
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour) - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Genetic algorithm parameters
population_size = 100
generations = 500
mutation_rate = 0.1

# Initialize population
population = [create_tour() for _ in range(population_size)]
fitness_scores = [fitness(tour) for tour in population]

# Evolution loop
for _ in range(generations):
    new_population = []
    sorted_pop = sorted(zip(population, fitness_scores), key=lambda x: x[1][0], reverse=True)
    # Elitism: carry the best individual to the next generation
    new_population.append(sorted_pop[0][0])
    while len(new_population) < population_size:
        # Tournament selection and crossover
        parent1 = min(random.sample(sorted_pop, 3), key=lambda x: x[1][0])[0]
        parent2 = min(random.sample(sorted_pop, 3), key=lambda x: x[1][0])[0]
        child = crossover(parent1, parent2)
        mutate(child, mutation_rate)
        new_population.append(child)
    population = new_population
    fitness_scores = [fitness(tour) for tour in population]

best_tour = sorted(zip(population, fitness_scores), key=lambda x: x[1][0], reverse=True)[0]
print(f"Tour: {best_tour[0]}")
print(f"Total travel cost: {best_tour[1][1]}")
print(f"Maximum distance between consecutive cities: {1 / best_tour[1][0]}")