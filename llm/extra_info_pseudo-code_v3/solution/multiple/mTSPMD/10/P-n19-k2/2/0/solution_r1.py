import numpy as np
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Compute distance matrix
def distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                matrix[i, j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
    return matrix

dist_matrix = distance_matrix(list(cities.values()))

# Genetic Algorithm Parameters
population_size = 50
generations = 1000
mutation_rate = 0.1
elite_size = 5

# Initialize population with routes
def create_initial_population(dist_matrix, depot_indices):
    population = []
    num_cities = len(dist_matrix)
    cities_list = list(range(num_cities))
    
    for _ in range(population_size):
        random.shuffle(cities_list)
        route = [cities_list[i] for i in range(num_cities) if cities_list[i] not in depot_indices]
        population.append(route)
        
    return population

# Calculate cost of routes (2 agents considering depots)
def calculate_cost(route, depot0, depot1):
    split_idx = len(route) // 2
    robot0_route = [depot0] + route[:split_idx] + [depot0]
    robot1_route = [depot1] + route[split_idx:] + [depot1]
    
    cost0 = sum(dist_matrix[robot0_route[i]][robot0_route[i+1]] for i in range(len(robot0_route)-1))
    cost1 = sum(dist_matrix[robot1_route[i]][robot1_route[i+1]] for i in range(len(robot1_route)-1))
    return cost0 + cost1, robot0_route, cost0, robot1_route, cost1

# Genetic operators
def breed(parent1, parent2):
    """Breeds two routes using ordered crossover."""
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    
    filled_positions = set(range(start, end+1))
    fill_idx = (end + 1) % len(parent1)
    
    for gene in parent2:
        if gene not in child:
            while fill_idx in filled_positions:
                fill_idx = (fill_idx + 1) % len(parent1)
            child[fill_idx] = gene
            filled_positions.add(fill_idx)
    
    return child

def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Evolution process
def evolve(population, depot0, depot1):
    ranked_population = sorted((calculate_cost(individual, depot0, depot1), individual) for individual in population)
    new_population = [ind for _, ind in ranked_population[:elite_size]]
    
    while len(new_population) < population_size:
        if random.random() < 0.7:
            par1, par2 = random.sample(new_population, 2)
            child = breed(par1, par2)
        else:
            child = random.choice(new_population)
        child = mutate(child, mutation_rate)
        new_population.append(child)
    
    return new_population, ranked_population[0][0]

# Simulation
population = create_initial_population(dist_matrix, {0, 1})
depot0, depot1 = 0, 1

for gen in range(generations):
    population, best = evolve(population, depot0, depot1)
    if gen % 100 == 0:  # Print every 100 generations
        print(f'Generation {gen}, Best Cost: {best[0]}')

best_cost, robot0_tour, robot0_cost, robot1_tour, robot1_cost = best

print(f'Final Best Tours and Costs:')
print(f'Robot 0 Tour: {robot0_tour}')
print(f'Robot 0 Total Travel Cost: {robot0_cost}')
print(f'Robot 1 Tour: {robot1_tour}')
print(f'Robot 1 Total Travel Cost: {robot1_cost}')
print(f'Overall Total Travel Cost: {best_cost}')