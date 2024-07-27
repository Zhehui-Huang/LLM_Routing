import numpy as np
import random

# Constants
CITIES = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}
ROBOT_COUNT = 4
DEPOTS = [0, 1, 2, 3]

# Genetic Algorithm Parameters
POP_SIZE = 100
MAX_GENERATIONS = 500
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_cost(chromosome):
    cost = 0
    start_index = 0
    
    for index in range(1, len(chromosome)):
        if chromosome[index] < 0:
            depot = DEPOTS[-chromosome[index] - 1]
            cost += distance(CITIES[chromosome[start_index]], CITIES[depot])
            start_index = index + 1
        else:
            cost += distance(CITIES[chromosome[start_index]], CITIES[chromosome[index]])
            start_index = index

    return cost

def initial_chromosome():
    cities = list(CITIES.keys())[4:]  # Exclude depots from cities
    random.shuffle(cities)
    chromosome = [0] + cities + [-1] * (ROBOT_COUNT - 1)  # Start from depot 0, ends are free
    return chromosome

def crossover(chromosome1, chromosome2):
    size = len(chromosome1)
    child = [-1] * size
    pos_a, pos_b = sorted(random.sample(range(size), 2))
    middle_c1 = chromosome1[pos_a : pos_b]
    filter_set = set(middle_c1)
    child[pos_a:pos_b] = middle_c1

    filler = [item for item in chromosome2 if item not in filter_set]
    child[:pos_a] = filler[:pos_a]
    child[pos_b:] = filler[pos_a:]

    return child

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm():
    population = [initial_chromosome() for _ in range(POP_SIZE)]
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(MAX_GENERATIONS):
        new_population = []
        
        for _ in range(POP_SIZE):
            if random.random() < CROSSOVER_RATE:
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                child = crossover(parent1, parent2)
            else:
                child = random.choice(population).copy()
            
            mutate(child, MUTATION_RATE)
            new_population.append(child)
        
        population = new_population
        current_best = min(population, key=total_route_cost)
        current_cost = total_route_cost(current_best)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best
        
        if generation % 100 == 0:
            print(f"Generation {generation}: Best Cost {best_cost}")
    
    return best_solution

best_tour = genetic_algorithm()
print("Best Tour:", best_tour)
print("Total Cost:", total_route_cost(best_tour))