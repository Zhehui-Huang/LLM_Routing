import numpy as np
from itertools import permutations
from random import randint, shuffle, sample, random
from math import sqrt

# Helper function to calculate the Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Initialize parameters for the genetic algorithm
number_of_robots = 2
population_size = 40
generations = 1000
mutation_rate = 0.1
crossover_rate = 0.8

def init_population(city_list, pop_size):
    population = []
    for _ in range(pop_size):
        route = sample(city_list, len(city_list))
        splice_idx = sorted(sample(range(1, len(city_list)), number_of_robots - 1))
        for idx in splice_idx:
            route.insert(idx, -1)
        population.append(route)
    return population

def calculate_fitness(route):
    total_cost = 0
    start_idx = 0
    distances = []
    for i in range(len(route)):
        if route[i] == -1 or i == len(route) - 1:
            if i == len(route) - 1: i += 1
            segment = route[start_idx:i]
            if segment:
                segment_cost = 0
                for j in range(len(segment) - 1):
                    segment_cost += euclidean_distance(*cities[segment[j]], *cities[segment[j+1]])
                total_cost += segment_cost
                distances.append(segment_cost)
            start_idx = i + 1
    return total_cost, distances

def select_parents(population):
    sorted_pop = sorted(population, key=lambda x: calculate_fitness(x)[0])
    return sorted_pop[:2]

def crossover(parent1, parent2):
    child1, child2 = parent1[:], parent2[:]
    if random() < crossover_rate:
        index1, index2 = sorted(sample(range(len(parent1)), 2))
        middle1 = parent1[index1:index2]
        middle2 = parent2[index1:index2]
        child1 = child1[:index1] + middle2 + child1[index2:]
        child2 = child2[:index1] + middle1 + child2[index2:]
        child1 = [i for n, i in enumerate(child1) if i not in child1[:n]]
        child2 = [j for n, j in enumerate(child2) if j not in child2[:n]]
    return child1, child2

def mutate(route):
    if random() < mutation_rate:
        idx1, idx2 = sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]

def genetic_algorithm():
    city_list = list(cities.keys())
    population = init_population(city_list, population_size)
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    
    best_solution = min(population, key=lambda x: calculate_fitness(x)[0])
    best_cost, split_costs = calculate_fitness(best_solution)
    return best_solution, best_cost, split_costs

# Solve the problem
best_route, total_cost, individual_costs = genetic_algorithm()

# Format the output
robot_tours = []
current_tour = []
for r in best_route:
    if r == -1:
        if current_tour:
            robot_tours.append(current_tour)
            current_tour = []
    else:
        current_tour.append(r)
if current_tour:
    robot_tours.append(current_tour)

for i, tour in enumerate(robot_tours):
    print(f"Robot {i} Tour: {[0] + tour + [0]}")
    print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")