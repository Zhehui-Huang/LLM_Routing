import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Initialize parameters
num_robots = 4
depots = [0, 1, 2, 3]
non_depot_cities = [i for i in cities if i not in depots]
population_size = 100
num_generations = 1000
mutation_rate = 0.1
crossover_rate = 0.8

# Helper function to calculate the Euclidean distance
def calc_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Genetic algorithm functions
def create_initial_solution():
    route = non_depot_cities[:]
    random.shuffle(route)
    portions = sorted(random.sample(range(1, len(route)), num_robots-1))
    routes = [route[prev:p] for prev, p in zip([0]+portions, portions+[None])]
    routes = [[depots[i]] + routes[i] + [depots[i]] for i in range(num_robots)]
    return routes

def calculate_total_distance(routes):
    cost = 0
    for route in routes:
        for i in range(len(route)-1):
            cost += calc_distance(route[i], route[i+1])
    return cost

def crossover(parent1, parent2):
    child_routes = []
    for idx in range(num_robots):
        if random.random() < crossover_rate:
            cut1, cut2 = sorted(random.sample(range(len(parent1[idx])-2), 2))
            main_part = parent1[idx][cut1+1:cut2+1]
            remaining = [city for city in parent2[idx] if city not in main_part]
            new_route = remaining[:cut1+1] + main_part + remaining[cut1+1:]
            child_routes.append([depots[idx]] + new_route + [depots[idx]])
        else:
            child_routes.append(parent1[idx])
    return child_routes

def mutate(routes):
    for idx in range(num_robots):
        if random.random() < mutation_rate:
            a, b = sorted(random.sample(range(1, len(routes[idx])-1), 2))
            routes[idx][a], routes[idx][b] = routes[idx][b], routes[idx][a]
    return routes

# Initialize population
population = [create_initial_solution() for _ in range(population_size)]
best_cost = float('inf')
best_solution = None

# Genetic Algorithm execution
for generation in range(num_generations):
    # Evaluate fitness
    population.sort(key=calculate_total_distance)
    current_best = population[0]
    current_cost = calculate_total_distance(current_best)
    if current_cost < best_cost:
        best_cost = current_cost
        best_solution = current_best

    # Selection (using elitism and tournament selection)
    next_population = population[:10]  # Elitism
    tournament_size = 5
    while len(next_population) < population_size:
        participants = random.sample(population, tournament_size)
        winner = min(participants, key=calculate_total_distance)
        next_population.append(winner)

    # Crossover and mutation
    population = []
    for _ in range(population_size//2):
        parent1, parent2 = random.sample(next_population, 2)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        population.append(mutate(child1))
        population.append(mutate(child2))

# Output the best result
overall_cost = calculate_total_distance(best_solution)
print("Best solution found:")
for idx in range(num_robots):
    print(f"Robot {idx} Tour: {best_solution[idx]}")
    print(f"Robot {idx} Total Travel Cost: {calculate_total_distance([best_solution[idx]])}")

print(f"Overall Total Travel Cost: {overall_cost}")