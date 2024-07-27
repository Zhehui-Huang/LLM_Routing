import numpy as np
import random

coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def create_route():
    cities = list(coordinates.keys())
    cities.remove(0) # remove the depot city from the list
    random.shuffle(cities)
    return [0] + cities

def calculate_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return cost

def crossover_and_mutate(parent1, parent2):
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    if random.random() < 0.1:  # mutation chance
        swap_indices = random.sample(range(1, len(child)), 2)
        child[swap_indices[0]], child[swap_indices[1]] = child[swap_indices[1]], child[swap_indices[0]]
    return child

def genetic_algorithm(population_size, generations):
    population = [create_route() for _ in range(population_size)]
    for _ in range(generations):
        # Evaluate the fitness
        costs = [calculate_cost(individual) for individual in population]
        sorted_population = [x for _, x in sorted(zip(costs, population), key=lambda pair: pair[0])]
        
        # Selection and creating a new population
        new_population = sorted_population[:2]  # Elitism: carry forward the best solutions
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(sorted_population[:population_size//2], 2)
            child = crossover_and_mutate(parent1, parent2)
            new_population.append(child)
        
        population = new_population
    
    best_route = population[0]
    best_cost = calculate_cost(best_route)
    return best_route, best_cost

best_route, best_cost = genetic_algorithm(100, 200)  # 100 individuals, 200 generations

print("Best Route:", best_with_depot)
print("Total Travel Cost:", best_cost)