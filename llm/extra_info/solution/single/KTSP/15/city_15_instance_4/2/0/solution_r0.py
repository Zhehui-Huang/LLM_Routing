import math
import random
from itertools import permutations

# Define cities' coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return total_distance

def genetic_algorithm(cities, population_size=100, generations=1000):
    def create_initial_population():
        population = []
        for _ in range(population_size):
            tour = [0] + random.sample(range(1, len(cities)), 11)
            population.append(tour + [0])
        return population

    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(1, 12), 2))
        child = [None] * len(parent1)
        child[start:end] = parent1[start:end]
        child_filled = set(parent1[start:end])
        pointer = 0
        for city in parent2:
            if city not in child_filled:
                while child[pointer] is not None:
                    pointer += 1
                child[pointer] = city
        return child
    
    def mutate(tour, mutation_rate=0.1):
        if random.random() < mutation_rate:
            i, j = sorted(random.sample(range(1, 12), 2))
            tour[i], tour[j] = tour[j], tour[i]
        return tour
    
    population = create_initial_population()
    for _ in range(generations):
        population.sort(key=calculate_total_distance)
        new_population = population[:2]  # Elitism
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    
    best_route = sorted(population, key=calculate_total_distance)[0]
    return best_route, calculate_total_distance(best_route)

# Run genetic algorithm
best_tour, best_cost = genetic_greaterm_algorithm(cities)

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)