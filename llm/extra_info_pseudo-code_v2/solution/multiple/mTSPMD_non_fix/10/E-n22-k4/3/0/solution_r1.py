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

def route_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += distance(CITIES[route[i-1]], CITIES[route[i]])
    return cost

def chromosome_to_routes(chromosome):
    routes = []
    current_route = []
    for gene in chromosome:
        if gene >= 0:
            current_route.append(gene)
        else:
            current_route.append(DEPOTS[-gene-1])
            routes.append(current_route)
            current_route = []
    return routes

def evaluate(chromosome):
    routes = chromosome_to_routes(chromosome)
    return sum(route_cost(route) for route in routes)

def initial_chromosome():
    cities = list(set(CITIES.keys()) - set(DEPOTS))
    random.shuffle(cities)
    parts = np.array_split(cities, ROBOT_COUNT)
    chromosome = []
    for i, part in enumerate(parts):
        chromosome.extend([-i] + list(part))
    return chromosome

def crossover(parent1, parent2):
    child = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
    return child

def mutate(chromosome):
    i = random.randint(0, len(chromosome) - 1)
    j = random.randint(0, len(chromosome) - 1)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

def genetic_algorithm():
    population = [initial_chromosome() for _ in range(POP_SIZE)]
    best_solution = None
    best_cost = float('inf')
    
    for generation in range(MAX_GENERATIONS):
        new_population = []
        
        for i in range(POP_SIZE):
            child = crossover(random.choice(population), random.choice(population))
            mutate(child)
            new_population.append(child)
        
        population = new_population
        current_best = min(population, key=evaluate)
        current_cost = evaluate(current_before)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_best
        
    return chromosome_to_routes(best_solution), best_cost

best_routes, total_cost = genetic_look()
for i, route in enumerate(best_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {int(route_cost(route))}")

print(f"Overall Total Travel Cost: {int(total_cost)}")