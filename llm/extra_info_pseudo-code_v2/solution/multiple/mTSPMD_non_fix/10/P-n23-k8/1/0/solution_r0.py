import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

robots = 8
depot = 0

def generate_initial_population(size, cities):
    population = []
    for _ in range(size):
        perm = list(cities)
        random.shuffle(perm)
        population.append([depot] + perm + [depot])
    return population

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def fitness(chromosome):
    return sum(calculate_cost(chromosome[i:i+2]) for i in range(len(chromosome)-1))

def selection(population, size):
    sorted_population = sorted(population, key=fitness)
    return sorted_population[:size]

def crossover(parent1, parent2):
    size = len(parent1)
    point1, point2 = sorted(random.sample(range(size), 2))
    child = [-1] * size
    middle = parent1[point1:point2]
    child[point1:point2] = middle
    fill = [item for item in parent2 if item not in middle]
    child[:point1] = fill[:point1]
    child[point2:] = fill[point1:]
    return child

def mutate(chromosome):
    idx1, idx2 = sorted(random.sample(range(len(chromosome)), 2))
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

def genetic_algorithm(cities, population_size, generations):
    population = generate_initial_population(population_size, cities)
    for _ in range(generations):
        population = selection(population, len(population) // 2)
        offsprings = []
        for i in range(0, len(population), 2):
            if i+1 < len(population):
                offsprings.append(crossover(population[i], population[i+1]))
        population += offsprings
        population = [mutate(chrom) for chrom in population]
    
    best_solution = min(population, key=fitness)
    best_cost = fitness(best_solution)
    return best_solution, best_cost

# Running the genetic algorithm to find the optimal tours
best_solution, best_cost = genetic_algorithm(cities, 100, 500)
print("Best Tours (Depots Included):", best_solution)
print("Minimum Total Cost:", best_cost)