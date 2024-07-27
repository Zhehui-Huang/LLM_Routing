import numpy as np
import random

# Coordinates for each city (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize parameters
num_robots = 2
depots = [0, 1]
num_cities = len(coordinates)
population_size = 40
generations = 500
mutation_rate = 0.15
crossover_rate = 0.85

# Utility functions
def create_initial_population():
    population = []
    for _ in range(population_size):
        perm = np.random.permutation(range(2, num_cities))
        split = random.randint(1, len(perm) - 1)
        chromosome = perm[:split].tolist() + [-1] + perm[split:].tolist()
        chromosome = [0] + chromosome + [1]
        population.append(chromosome)
    return population

def fitness(chromosome):
    total_cost = 0
    current_depot = depots[0]
    current_route = []
    for gene in chromosome:
        if gene == -1:
            current_depot = depots[1]
            current_route = []
        else:
            if current_route:
                total_cost += euclidean_distance(coordinates[current_route[-1]], coordinates[gene])
            current_route.append(gene)
    return -total_cost

def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return [parent1.copy(), parent2.copy()]
    size = len(parent1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    child1 = parent1[:cxpoint1] + parent2[cxpoint1:cxpoint2] + parent1[cxpoint2:]
    child2 = parent2[:cxpoint1] + parent1[cxpoint1:cxpoint2] + parent2[cxpoint2:]
    return [child1, child2]

def mutate(chromosome):
    if random.random() < mutation_rate:
        idx1, idx2 = sorted(random.sample(range(1, len(chromosome)-1), 2))
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

# Genetic Algorithm
population = create_initial_population()
for _ in range(generations):
    population = sorted(population, key=fitness)
    next_generation = population[:2]  # Elitism: carry forward the best 2 solutions
    while len(next_generation) < population_size:
        parents = random.sample(population[:10], 2)  # Tournament selection
        for child in crossover(parents[0], parents[1]):
            mutate(child)
            next_generation.append(child)
    population = next_generation

# Extract best solution
best_solution = sorted(population, key=fitness)[0]

# Print result
current_depot = 0
tour = [0]
cost = 0
total_cost = 0
for city in best_solution:
    if city == -1:
        tour.append(current_depot)
        print(f"Robot {current_deopard} Tour: {tour}")
        print(f"Robot {current_depot} Total Travel Cost: {cost}")
        total_cost += cost
        current_depot = 1 - current_depot
        tour = [current_depot]
        cost = 0
    else:
        if len(tour) > 1:
            cost += euclidean_distance(coordinates[tour[-1]], coordinates[city])
        tour.append(city)

# Output the results
print("Overall Total Travel Cost:", total_cost)