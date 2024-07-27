import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize population with random solutions
def generate_population(size, chromosome_length):
    return [[random.choice(range(chromosome_length)) for _ in range(chromosome_length)] for _ in range(size)]

# Calculate the fitness of a chromosome (lower is better)
def calculate_fitness(chromosome):
    total_distance = 0
    for i in range(len(chromosome) - 1):
        total_distance += distance(chromosome[i], chromosome[i+1])
    total_distance += distance(chromosome[-1], chromosome[0])  # complete the tour
    return total_distance

# Selection process (tournament selection)
def tournament_selection(population, k=3):
    best = None
    for i in range(k):
        ind = random.choice(population)
        if best is None or calculate_fitness(ind) < calculate_fitness(best):
            best = ind
    return best

# Crossover (Partially Matched Crossover, PMX)
def pmx(parent1, parent2):
    size = len(parent1)
    p1, p2 = [0]*size, [0]*size

    # Initialize the position of each indices in individuals
    for i in range(size):
        p1[parent1[i]] = i
        p2[parent2[i]] = i
    # Choose crossover points
    cx1, cx2 = sorted(random.sample(range(size), 2))
    # Apply crossover between cx1 and cx2
    for i in range(cx1, cx2):
        temp1 = parent1[i]
        temp2 = parent2[i]
        parent1[i], parent1[p1[temp2]] = temp2, temp1
        parent2[i], parent2[p2[temp1]] = temp1, temp2
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]
    return parent1, parent2

# Mutation (swap mutation)
def mutate(chromosome, mutation_rate=0.02):
    for swapped in range(len(chromosome)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(chromosome))
            chromosome[swapped], chromosome[swap_with] = chromosome[swap_with], chromosome[swapped]
    return chromosome