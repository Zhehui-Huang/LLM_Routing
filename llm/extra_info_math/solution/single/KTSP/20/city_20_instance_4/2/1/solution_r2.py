import numpy as np
from scipy.spatial.distance import euclidean

# Define the cities coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the distance matrix
n_cities = len(cities_coordinates)
dist_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i][j] = euclidean(cities_coordinates[i], cities_coordinates[j])

# Genetic Algorithm parameters
pop_size = 100       # Population size
generations = 500    # Number of generations, reduced for quick runs
mutation_rate = 0.2  # Mutation rate, increased for higher diversity

def create_route():
    route = np.random.choice(range(1, n_cities), size=15, replace=False)
    return [0] + list(route) + [0]

def initial_population(pop_size):
    return [create_route() for _ in range(pop_size)]

def route_cost(route):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

def breed(parent1, parent2):
    gene_a = np.random.randint(1, len(parent1)-1)
    gene_b = np.random.randint(1, len(parent1)-1)

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    child_p1 = parent1[start_gene:end_gene]
    child_p2 = [item for item in parent1 + parent2 if item not in child_p1 and item != 0]
    child = [0] + child_p1 + child_p2[:15 - len(child_p1)] + [0]
    
    return child

def mutate(individual, mutation_rate):
    for swapped in range(1, len(individual) - 1):
        if np.random.random() < mutation_rate:
            swap_with = np.random.randint(1, len(individual) - 1)
            individual[swapped], individual[swap_with] = individual[swap_with], individual[swapped]

# Genetic Algorithm Main Procedure 
population = initial_population(pop_size)
for _ in range(generations):
    population = sorted(population, key=route_cost)
    elite_size = int(0.2 * pop_size)
    elite = population[:elite_size]
    new_gen = elite[:]
    
    while len(new_gen) < pop_size:
        parent1 = np.random.choice(elite)
        parent2 = np.random.choice(elite)
        child = breed(parent1, parent2)
        mutate(child, mutation_rate)
        new_gen.append(child)
    
    population = new_gen

best_route = sorted(population, key=route_cost)[0]
best_cost = route_cost(best_route)

print("Tour:", best_route)
print("Total travel cost:", best_cost)