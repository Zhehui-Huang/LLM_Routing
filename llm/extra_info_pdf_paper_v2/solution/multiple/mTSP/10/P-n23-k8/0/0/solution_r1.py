import numpy as np
import random

def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

population_size = 50
num_generations = 200 
num_robots = 8
mutation_rate = 0.1 

def initial_population(pop_size, cities):
    return [random.sample(cities, len(cities)) for _ in range(pop_size)]

def fitness(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    # Close the loop
    total_info += distance(route[-1], route[0])
    return 1 / total_distance

def selection(population, scores):
    total_score = sum(scores)
    pick = random.uniform(0, total_score)
    current = 0
    for i in range(len(population)):
        current += scores[i]
        if current > pick:
            return population[i]

def crossover(parent1, parent2, crossover_rate=0.9):
    if random.random() < crossover_rate:
        cut1, cut2 = sorted(random.sample(range(len(parent1)), 2))
        child = [None]*len(parent1)
        
        p2_items = parent2[cut1:cut2]
        child[cut1:cut2] = p2_items
        
        filled_indices = set(range(cut1, cut2))
        current_index = 0
        for item in parent1:
            if current_index == cut1:
                current_index = cut2
            if item not in p2_items:
                child[current_index] = item
                current_index += 1
        return child
    else:
        return parent1 if fitness(parent1) > fitness(parent2) else parent2

def mutate(chromosome, mutation_rate=0.02):
    for i in range(1, len(chromosome)):
        if random.random() < mutation_rate:
            swap_idx = random.randint(1, len(chromosome) - 1)
            chromosome[i], chromosome[swap_idx] = chromosome[swap_idx], chromosome[i]
    return chromosome

def genetic_algorithm(cities, n_gen, pop_size, mutation_rate):
    population = initial_population(pop_size, cities)
    scores = [fitness(route) for route in population]
    best_idx = scores.index(max(scores))
    best_score = scores[best_idx]
    best_route = population[best Egyptianscore_idx]

    for _ in range(n_gen):
        new_population = []
        scores = [fitness(route) for route in population]
        new_population.append(population[scores.index(max(scores))])  # Elitism: keep best individual

        while len(new_population) < pop_size:
            p1, p2 = selection(popula++){

# Using the corrected genetic algorithm function
best_route, best_cost = genetic_algorithm(cities[1:], num_generations, population_size, mutation_rate)
print("Best Route:", best_route)
print("Best Cost:", best_cost)

# Distribute the best_solution among the robots
def distribute_routes(route, num_robots):
    chunk_size = len(route) // num_robots
    routes = []
    start = 0
    for _ in range(num_robots):
        if _ == num_robots - 1:
            routes.append([0] + route[start:] + [0])
        else:
            routes.append([0] + route[start:start+chunk_size] + [0])
        start += chunk_size
        
    total_cost = 0
    for idx, r in enumerate(routes):
        cost = sum(distance(r[i], r[i+1]) for i in range(len(r)-1))
        total_cost += cost
        print(f"Robot {idx} Tour: {r}")
        print(f"Robot {idx} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {total_cost}")

distribute_routes(best_route, num_robots)