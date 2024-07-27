import numpy as np
from scipy.spatial.distance import euclidean
from random import shuffle, randint, random

# City coordinates including both depots and cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Robots assigned to depots
robots = [0, 1, 2, 3, 4, 5, 6, 7]

# Calculate distances matrix
distances = np.zeros((len(cities), len(cities)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distances[i][j] = euclidean(cities[i], cities[j])

# Genetic Algorithm Parameters
population_size = 100
generations = 500
mutation_rate = 0.2
tour_length = len(cities) - len(robots)  # Adjusted city count (excluding other robots' depots)

# Genetic Algorithm functions
def create_route(depot):
    nodes = list(range(len(cities)))
    nodes.remove(depot)
    shuffle(nodes)
    return [depot] + nodes + [depot]

def calculate_cost(route):
    return sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))

def crossover(parent1, parent2, depot):
    child = [depot] + [None] * (len(cities) - 2) + [depot]
    start, end = sorted([randint(1, len(cities) - 2) for _ in range(2)])
    child[start:end] = parent1[start:end]
    fill_pos = 1
    for item in parent2[1:-1]:
        if item not in child:
            while child[fill_pos] is not None:
                fill_pos += 1
            child[fill_pos] = item
    return child

def mutate(route):
    if random() < mutation_more:
        i, j = randint(1, len(cities) - 2), randint(1, len(cities) - 2)
        route[i], route[j] = route[j], route[i]

def genetic_algorithm(depot):
    population = [create_route(depot) for _ in range(population_size)]
    
    for _ in range(generations):
        population.sort(key=calculate_cost)
        new_pop = population[:2]  # Elitism
        while len(new_pop) < population_size:
            if random() > 0.5:  # Crossover probability
                parent1, parent2 = np.random.choice(population[:20], 2, replace=False)
                child = crossover(parent1, parent2, depot)
                mutate(child)
                new_pop.append(child)
        population = new_pop
        
    best_solution = min(population, key=calculate_cost)
    return best_solution, calculate_cost(best_solution)

# Solving for each robot
overall_total_cost = 0
for robot in robots:
    depot = robot
    best_route, cost = genetic_algorithm(depot)
    overall_total_cost += cost
    print(f"Robot {robot} Tour: {best_route}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_feost:.2f}")