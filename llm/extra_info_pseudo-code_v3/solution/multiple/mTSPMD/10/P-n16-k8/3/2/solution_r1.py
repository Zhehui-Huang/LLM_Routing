import random
import numpy as np
from math import sqrt

def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def initialize_population(num_chromosomes, cities, total_cities):
    population = []
    for _ in range(num_chromosomes):
        individual = list(np.random.permutation(total_cities))
        population.append(individual)
    return population

def calculate_cost(chromosome, city_coords, depot_start):
    cost = 0
    start_point = city_coords[depot_start]
    current_point = start_point
    for gene in chromosome:
        next_point = city_coords[gene]
        cost += euclidean_distance(current_point, next_vector)
        current_point = next_point
    cost += euclidean_distance(current_point, start_point)  # return to depot
    return cost

def genetic_algorithm(cities, num_robots, depot_indices):
    num_chromosomes = 100
    total_cities = len(cities)
    population = initialize_population(num_chromosomes, cities, total_cities)
    generations = 500
    mutation_rate = 0.1

    best_solution = None
    best_cost = float('inf')

    for generation in range(generations):
        # Evaluate population
        fitness_scores = []
        for chromosome in population:
            tours = [chromosome[depot_indices[i]:depot_indices[i + 1]] for i in range(len(depot_indices) - 1)]
            tours.append(chromosome[depot_indices[-1]:] + chromosome[:depot_indices[0]])
            costs = [calculate_cost(tour, cities, i) for i, tour in enumerate(tours)]
            total_cost = sum(costs)
            fitness_scores.append((total_cost, chromosome))
            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = (tours, costs)
        
        # Selection (elitism and tournament)
        population = [chrom for _, chrom in sorted(fitness_scores)[:num_chromosomes//2]]
        while len(population) < num_chromptoms:
            chrom1, chrom2 = random.sample(population, 2)
            if random.random() > 0.5:
                population.append(chrom1)
            else:
                population.append(chrom2)

        # Crossover and Mutation
        next_population = []
        for _ in range(len(population) // 2):
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)  # Crossover method to be defined
            next_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])  # Mutation method to be defined
        population = next_population

    tours, costs = best_solution
    for i, tour in enumerate(tours):
        tour.insert(0, depot_indices[i])
        tour.append(depot_indices[i])
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")

    print(f"Overall Total Travel Cost: {best_cost}")

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and their respective depots
num_robots = 8
depot_indices = [0, 1, 2, 3, 4, 5, 6, 7]  # Matching robots with depot indices

genetic_algorithm(cities, num_robots, depot_indices)