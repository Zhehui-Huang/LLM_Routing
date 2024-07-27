import random
import numpy as np
from scipy.spatial import distance_matrix

# Step 1: Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52),
    2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69), 16: (38, 46), 
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of robots and depots
num_robots = 2
depots = [0, 1]  # Robot 0 starts at city 0, Robot 1 starts at city 1

# Step 2: Calculate distance matrix between all cities
city_locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(city_locations, city_locations)

# Step 3 and 4: Initial chromosome and Fitness Function
def create_initial_population(pop_size):
    population = []
    for _ in range(pop_size):
        nodes = list(cities.keys())[2:]  # excluding depots
        random.shuffle(nodes)
        split_point = random.randint(1, len(nodes) - 1)
        population.append((nodes, split_point))
    return population

def total_route_cost(route):
    return sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def chromosome_fitness(chromosome):
    nodes, split_point = chromosome
    tour1 = [0] + nodes[:split_point] + [0]
    tour2 = [1] + nodes[split_point:] + [1]
    cost1 = total_route_cost(tour1)
    cost2 = total_route_cost(tour2)
    total_cost = cost1 + cost2
    return total_cost, tour1, cost1, tour2, cost2

# Genetic algorithm methods: crossover, mutation, and main loop
def crossover(parent1, parent2):
    nodes1, point1 = parent1
    nodes2, point2 = parent2
    new_point = random.randint(1, len(nodes1) - 1)
    child_nodes = nodes1[:new_point] + nodes2[new_point:]
    return (child_nodes, new_point)

def mutate(chromosome, rate=0.2):
    nodes, point = chromosome
    if random.random() < rate:
        i, j = random.sample(range(len(nodes)), 2)
        nodes[i], nodes[j] = nodes[j], nodes[i]
    if random.random() < rate:
        point = random.randint(1, len(nodes) - 1)
    return (nodes, point)

def genetic_algorithm(pop_size=100, generations=300):
    population = create_initial_population(pop_size)
    best = None
    best_fitness = float('inf')

    for _ in range(generations):
        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)
        population = new_pop
        population.sort(key=lambda x: chromosome_fitness(x)[0])
        if chromosome_fitness(population[0])[0] < best_fitness:
            best = population[0]
            best_fitness = chromosome_fitness(best)[0]

    return best

# Run the genetic algorithm
best_chromosome = genetic_algorithm()
best_fitness, best_tour1, best_cost1, best_tour2, best_cost2 = chromosome_fitness(best_chromosome)

# Providing results
print("Robot 0 Tour:", best_tour1)
print("Robot 0 Total Travel Cost:", best_cost1)
print("Robot 1 Tour:", best_tour2)
print("Robot 1 Total Travel Cost:", best_cost2)
print("Overall Total Travel Cost:", best_cost1 + best_cost2)