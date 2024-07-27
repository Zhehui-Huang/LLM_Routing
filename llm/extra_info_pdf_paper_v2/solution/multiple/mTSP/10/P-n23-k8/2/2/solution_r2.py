import numpy as np
from math import sqrt
import random

# Coordinates of the cities including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def calculate_distance(tour):
    return sum(sqrt((cities[tour[i]][0] - cities[tour[i + 1]][0]) ** 2 + (cities[tour[i]][1] - cities[tour[i + 1]][1]) ** 2) for i in range(len(tour) - 1))

def create_tour():
    nodes = list(cities.keys())[1:]
    random.shuffle(nodes)
    return [0] + nodes + [0]

def create_initial_population(size, num_robots):
    return [create_tour() for _ in range(size)]

def selection(population, num_robots):
    sorted_population = sorted(population, key=lambda tour: calculate_distance(tour))
    return sorted_population[:num_robots]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(1, len(parent1) - 2), 2))
    child = parent1[:start] + [city for city in parent2[start:end] if city not in parent1] + parent1[end:]
    child = [0] + [city for city in child if city != 0] + [0]  # Ensure the start and end at the depot
    return child

def mutate(tour, mutation_rate=0.05):
    for i in range(1, len(tour) - 2):
        if random.random() < mutation_rate:
            j = random.randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm(num_generations, num_robots, pop_size):
    population = create_initial_population(pop_size, num_robots)
    for generation in range(num_generations):
        new_population = selection(population, int(len(population) * 0.5))
        children = []
        while len(children) < len(population):
            parent1, parent2 = random.sample(new_population, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            children.append(child)
        population = new_population + children
    return selection(poplication, num_robots)

# Define key parameters
num_generations = 1000
num_robots = 8
population_size = 200

# Running GA to solve the problem
best_solutions = genetic_algorithm(num_generations, num_robots, population_size)
best_tours = [sol for sol in best_solutions]

# Calculating the cost for each robot and total cost
total_cost = 0
for i, tour in enumerate(best_tours):
    cost = calculate_distance(tour)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")