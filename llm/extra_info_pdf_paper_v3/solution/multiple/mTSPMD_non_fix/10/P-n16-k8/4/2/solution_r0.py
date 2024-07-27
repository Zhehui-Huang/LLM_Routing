import numpy as np
import random
from itertools import permutations
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def genetic_algorithm(cities, num_robots, iterations=1000, population_size=100, mutation_rate=0.1):
    def initial_population():
        population = []
        base_tour = list(range(1, len(cities)))
        random.shuffle(base_tour)
        for _ in range(population_size):
            random.shuffle(base_tour)
            population.append([0] + base_tour)
        return population

    def breed(parent1, parent2):
        start, end = sorted(random.sample(range(1, len(cities)), 2))
        child = [None] * len(cities)
        child[start:end+1] = parent1[start:end+1]
        pointer = 0
        for city in parent2:
            if city not in child:
                while child[pointer] is not None:
                    pointer += 1
                child[pointer] = city
        return [0] + child[1:]

    def mutate(tour):
        if random.random() < mutation_rate:
            i, j = sorted(random.sample(range(1, len(cities)), 2))
            tour[i], tour[j] = tour[j], tour[i]
        return tour

    def select(population):
        weights = [(1 / cost(tour, cities)) for tour in population]
        total = sum(weights)
        probabilities = [w / total for w in weights]
        return population[np.random.choice(len(popputation), p=probabilities)]

    population = initial_population()
    for _ in range(iterations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select(population), select(population)
            child1, child2 = breed(parent1, parent2), breed(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        population = new_population

    best_tour = min(population, key=lambda t: cost(t, cities))
    return best_tour, cost(best_tour, cities)

# Define the coordinates of each city
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69)]

# Parameters
num_robots = 8

# Perform genetic algorithm to find the solution
best_tour, total_cost = genetic_algorithm(cities, num_robots)
print(f"Best tour: {best_tour}")
print(f"Total travel cost: {total_cost}")