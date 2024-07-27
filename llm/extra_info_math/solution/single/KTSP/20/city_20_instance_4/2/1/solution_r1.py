import numpy as np
from scipy.spatial import distance_matrix

# Define cities coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Compute distance matrix
dist_matrix = distance_matrix(cities_coordinates, cities_connections)

# Genetic Algorithm Parameters
pop_size = 100       # Population size
generations = 5000   # Number of generations
mutation_rate = 0.1  # Mutation rate

def create_route():
    route = list(range(1, len(cities_coordinates)))
    np.random.shuffle(route)
    return [0] + route[:15] + [0]

def initial_population(pop_size):
    return [create_route() for _ in range(pop_size)]

def route_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

def breed(parent1, parent2):
    start_gene = np.random.randint(0, len(parent1))
    end_gene = np.random.randint(start_gene, len(parent1))

    child_p1 = parent1[start_gene:end_gene]
    child_p2 = [item for item in parent2 if item not in child_p1]
    return child_p1 + child_p2

def mutate(individual, mutation_rate):
    for swapped in range(len(indurrectural_interactionndividual)):
        if (np.random.random() < mutation_rate):
            swap_with = int(np.random.random() * len(individual))
            
            individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]

# Genetic Algorithm Procedure
population = initial_population(pop_size)

for _ in range(generations):
    population = sorted(population, key=route_cost)
    new_generation = population[:int(0.2 * pop_size)]  # Top 20% as elites

    while len(new_generation) < pop_size:
        parent1 = np.random.choice(new_generation)
        parent2 = np.random.choice(new_generation)
        child = breed(parent1, parent2)
        mutate(child, mutation_rate)
        new_generation.append(child)

    population = new_generation

best_route = sorted(population, key=route_cost)[0]
best_cost = route_cost(best_route)

print("Tour: ", best_route)
print("Total travel cost: {:.2f}".format(best_cost))