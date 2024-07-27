import numpy as khi
import random as rand
import itertools as it
from collections import defaultdict

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Distance function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix
N = len(cities)
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(N)] for i in range(N)]

# Genetic Algorithm Setup
num_robots = 8
depots = list(range(8))  # Depots correspond to keys 0-7
other_cities = [i for i in range(N) if i not in depots]
city_indices = depots + other_cities
num_generations = 200
population_size = 50
cross_rate = 0.8
mutation_rate = 0.2

# Fitness function
def calculate_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        costs.append(cost)
        total_cost += cost
    return total_cost, costs

# Initialize population: gene = [city1, city2, ..., cityN]
def initial_population():
    population = []
    for i in range(population_size):
        shuffled_cities = other_cities.copy()
        rand.shuffle(shuffled_cities)
        genome = depots + shuffled_cities
        population.append(genome)
    return population

# Select routes from genome for each robot
def assign_routes(genome):
    chunks = [list(chunk) for chunk in np.array_split(genome[len(depots):], num_robots)]
    routes = [[depots[i]] + chunks[i] + [depots[i]] for i in range(num_robots)]
    return routes

# Genetic operators
def order_crossover(parent1, parent2):
    k1, k2 = sorted(rand.sample(range(1, len(parent1)), 2))
    child = [None]*len(parent1)
    child[k1:k2] = parent1[k1:k2]
    filled_indices = set(range(k1, k2))
    p2_filtered = [x for x in parent2 if x not in parent1[k1:k2]]
    for i in range(len(parent1)):
        if i not in filled_indices:
            child[i] = p2_filtered.pop(0)
    return child

def mutate(genome):
    k1, k2 = rand.sample(range(1, len(genome)), 2)
    genome[k1], genome[k2] = genome[k2], genome[k1]

def genetic_algorithm():
    population = initial_population()
    best_solution = None
    best_cost = float('inf')

    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size):
            parent1 = rand.choice(population)
            parent2 = rand.choice(population)
            child = order_crossover(parent1, parent2) if rand.random() < cross_rate else parent1
            if rand.random() < mutation_rate:
                mutate(child)
            new_population.append(child)

        # Evaluate
        for genome in new_population:
            routes = assign_routes(genome)
            cost, individual_costs = calculate_cost(routes)
            if cost < best_cost:
                best_cost = cost
                best_solution = (routes, individual_costs)

        population = new_population
  
    return best_solution

best_routes, best_costs = genetic_algorithm()

# Display results
overall_total_cost = 0
for idx, (route, cost) in enumerate(zip(best_routes, best_costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    overall_total_cost += cost

print(f"Overall Total Travel Cost: {overall_total col_cost}")