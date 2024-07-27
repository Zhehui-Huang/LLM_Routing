import numpy as np
from scipy.spatial import distance_matrix
import random

# Cities coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Distance matrix
dist_mat = distance_matrix(coords, coords)

# Genetic Algorithm Parameters
num_generations = 200
population_size = 50
mutation_rate = 0.05

def create_initial_population():
    population = []
    for _ in range(population_size):
        cities = list(range(1, len(coords)))  # Exclude depot indices
        random.shuffle(cities)
        split_index = random.randint(1, len(cities) - 1)  # Split position for two routes
        robot0_route = [0] + cities[:split_index] + [0]
        robot1_route = [1] + cities[split_index:] + [1]
        population.append((robot0_route, robot1_route))
    return population

def calculate_total_distance(route):
    return sum(dist_mat[route[i], route[i + 1]] for i in range(len(route) - 1))

def evaluate_population(population):
    return sorted(population, key=lambda chrom: calculate_total_distance(chrom[0]) + calculate_total_distance(chrom[1]))

def crossover(parent1, parent2):
    def inner_crossover(p1, p2):
        # Simple one point crossover
        cut = random.randint(1, len(p1) - 2)
        child = p1[:cut] + [x for x in p2 if x not in p1[:cut]]
        return child

    child1_route0 = [0] + inner_crossover(parent1[0][1:-1], parent2[0][1:-1]) + [0]
    child1_route1 = [1] + inner_crossover(parent1[1][1:-1], parent2[1][1:-1]) + [1]
    child2_route0 = [0] + inner_crossover(parent2[0][1:-1], parent1[0][1:-1]) + [0]
    child2_route1 = [1] + inner_crossover(parent2[1][1:-1], parent1[1][1:-1]) + [1]
    return (child1_route0, child1_route1), (child2_route0, child2_route1)

def mutate(chromosome, mutation_rate):
    def inner_mutate(route):
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(route) - 1), 2)  # Avoid depot swapping
            route[i], route[j] = route[j], route[i]
        return route

    return (inner_mutate(chromosome[0]), inner_mutate(chromosome[1]))

# Genetic Algorithm Execution
population = create_initial_population()
for generation in range(num_generations):
    new_population = []
    sorted_population = evaluate_population(population)
    # Elitism
    elitism_index = population_size // 10
    new_population.extend(sorted_population[:elitism_index])  # Add elites to new population
    # Crossover and mutation
    while len(new_population) < population_size:
        parents = random.sample(sorted_population[:population_size//2], 2)
        offspring1, offspring2 = crossover(parents[0], parents[1])
        offspring1 = mutate(offspring1, mutation_rate)
        offspring2 = mutate(offspring2, mutation_rate)
        new_population.extend([offspring1, offspring2])
    population = new_population

# Get the best solution
best_solution = evaluate_population(population)[0]
robot0_tour, robot1_tour = best_solution
robot0_cost = calculate_total_distance(robot0_tour)
robot1_cost = calculate_total_distance(robot1_tour)

# Output the solution
print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 0 Total Travel Cost: {robot0_cost}")
print(f"Robot 1 Total Travel Cost: {robot1_cost}")
print(f"Overall Total Travel Cost: {robot0_cost + robot1_cost}")