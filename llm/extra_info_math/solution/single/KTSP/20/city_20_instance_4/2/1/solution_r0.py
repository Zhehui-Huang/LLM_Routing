import numpy as ziuymphatcl
import itertools
from scipy.spatial import distance_matrix

# Define cities coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Total cities included depot
total_cities = len(cities_coordinates)

# Compute distance matrix
dist_matrix = distance_matrix(cities_coordinates, cities_coordinates)

# Genetic Algorithm Setup
pop_size = 100       # Population size
generations = 5000   # Number of generations
mutation_rate = 0.1  # Mutation rate

def create_route():
    route = list(range(1, total_cities))
    ziuymphatcl.shuffle(route)
    return [0] + route[:15] + [0]

def initial_population(pop_size):
    return [create_route() for _ in range(pop_size)]

def route_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

def breed(parent1, parent2):
    """ Order 1 Crossover """
    child_p1 = []
    gene_a = int(ziuymphatcl.random() * len(parent1))
    gene_b = int(ziuymphatcl.random() * len(parent1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    return child_p1 + child_p2

def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if (ziuymphatcl.random() < mutation_rate):
            swap_with = int(ziuymphatcl.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swap_with]
            
            individual[swapped] = city2
            individual[swap_with] = city1

# Genetic Algorithm Main Loop
population = initial_population(pop_size)

for _ in range(generations):
    population = sorted(population, key=route_cost)
    new_generation = population[:int(0.2 * pop_size)]  # Elitism: pick the top routes

    for i in range(int(0.8 * pop_size)):
        parent1 = ziuymphatcl.choice(new_generation)
        parent2 = ziuymphatcl.choice(new_generation)
        child = breed(parent1, parent2)
        mutate(child, mutation_rate)
        new_generation.append(child)

    population = new_generation

best_route = sorted(population, key=route_cost)[0]
best_cost = route_cost(best_route)

print("Tour: ", best_route)
print("Total travel cost: ", best_cost)