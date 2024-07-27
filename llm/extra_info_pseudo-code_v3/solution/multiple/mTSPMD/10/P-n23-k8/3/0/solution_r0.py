import numpy as np
from scipy.spatial.distance import euclidean
from random import randint, sample, shuffle, choice
from itertools import permutations

# Locations of cities and depots
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depots = list(range(8))  # First 8 cities are depots

# Calculate distances between all pairs of cities
n_cities = len(locations)
dist_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i, j] = euclidean(locations[i], locations[j])

# Genetic Algorithm settings
population_size = 50
generations = 1000
mutation_rate = 0.1
crossover_rate = 0.7

def initialize_population():
    population = []
    cities = list(range(8, n_cities))  # city indices excluding depots
    for _ in range(population_size):
        shuffle(cities)
        chromosome = depots + cities
        population.append(chromosome)
    return population

def evaluate_tour(tour):
    cost = dist_matrix[tour[-1], tour[0]]
    for i in range(len(tour)-1):
        cost += dist_matrix[tour[i], tour[i+1]]
    return cost

def evaluate_population(population):
    costs = []
    for chromosome in population:
        assignments = [[] for _ in range(8)]  # assign cities to depots
        for i in range(8, len(chromosome)):
            nearest_depot = min(depots, key=lambda d: dist_matrix[d, chromosome[i]])
            assignments[nearest_depot].append(chromosome[i])
        costs.append(sum(evaluate_tour([depot]+assignment+[depot]) for depot, assignment in zip(depots, assignments)))
    return costs

def select_parents(population, costs):
    # Roulette Wheel Selection
    max_cost = max(costs)
    adjusted_fitness = [max_cost - cost for cost in costs]
    sum_fitness = sum(adjusted_fitness)
    pick = np.random.rand() * sum_fitness
    current = 0
    for chromosome, fitness in zip(population, adjusted_fitness):
        current += fitness
        if current > pick:
            return chromosome
    return population[-1]

def ordered_crossover(parent1, parent2):
    size = len(parent1)
    idx1, idx2 = sorted(sample(range(size), 2))
    offspring = [None] * size
    offspring[idx1:idx2] = parent1[idx1:idx2]
    place_idx = idx2
    for gene in parent2:
        if not gene in offspring:
            if place_idx >= size:
                place_idx = 0
            while offspring[place_idx] is not None:
                place_idx += 1
            offspring[place_idx] = gene
    return offspring

def mutate(chromosome):
    idx1, idx2 = sample(range(8, len(chromosome)), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]

def genetic_algorithm():
    population = initialize_population()
    best_solution = None
    best_cost = float('inf')

    for _ in range(generations):
        costs = evaluate_population(population)
        new_population = [population[np.argmin(costs)]]
        if min(costs) < best_cost:
            best_cost = min(costs)
            best_solution = population[np.argmin(costs)]

        while len(new_population) < population_size:
            parent1 = select_parents(population, costs)
            parent2 = select_parents(population, costs)
            if np.random.rand() < crossover_rate:
                offspring = ordered_crossover(parent1, parent2)
            else:
                offspring = parent1[:]
            if np.random.rand() < mutation_rate:
                mutate(offspring)
            new_population.append(offspring)
        
        population = new_population

    return best_solution, best_cost

best_solution, best_cost = genetic_algorithm()

# Extract tours for each robot
assignments = {d: [d] for d in depots}
for city in best_solution[8:]:
    nearest_depot = min(depots, key=lambda d: dist_matrix[d, city])
    assignments[nearest_depot].append(city)
for k, v in assignments.items():
    v.append(k)  # close the tour by returning to the depot

# Calculate individual and total travel costs
individual_costs = {k: evaluate_tour(v) for k, v in assignments.items()}
overall_cost = sum(individual_costs.values())

# Output the result
for robot_id, tour in assignments.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {individual_costs[robot_id]}")
print(f"Overall Total Travel Cost: {overall_cost}")