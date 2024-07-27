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
DEPOTS = [0]

# Genetic Algorithm Parameters
POP_SIZE = 100
MAX_GENERATIONS = 500
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(route):
    return sum(distance(CITIES[route[i]], CITIES[route[i+1]]) for i in range(len(route)-1))

def create_initial_population():
    population = []
    cities = list(CITIES.keys())[1:]  # Exclude depot city 0
    for _ in range(POP_SIZE):
        random.shuffle(cities)
        population.append([0] + cities)
    return population

def evaluate(chromosome):
    return total_distance(chromosome)

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    pos_a, pos_b = sorted(random.sample(range(1, size), 2))  # Ensure depot does not get disrupted
    child[pos_a:pos_b] = parent1[pos_a:pos_b]
    child_filter = set(child[pos_a:pos_b])
    fill_points = [item for item in parent2 if item not in child_filter and item != 0]
    child = [0] + fill_points[:pos_a-1] + child[pos_a:pos_b] + fill_points[pos_a-1:]
    return child

def mutate(chromosome):
    i, j = random.sample(range(1, len(chromosome)), 2)  # Ensure depot does not get moved
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(MAX_GENERATIONS):
        new_population = []
        
        for i in range(POP_SIZE):
            if random.random() < CROSSOVER_RATE:
                parent1 = random.choice(population)
                parent2 = random.choice(population)
                child = crossover(parent1, parent2)
            else:
                child = random.choice(population).copy()
            if random.random() < MUTATION_RATE:
                mutate(child)
            new_population.append(child)
        
        population = sorted(new_population, key=evaluate)[:POP_SIZE]
        current_best = population[0]
        current_cost = evaluate(current_best)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best
        
    return best_solution, best_cost

best_solution, total_cost = genetic_algorithm()
print("Best Solution Tour:", best_solution)
print("Best Solution Total Travel Cost:", total_cost)