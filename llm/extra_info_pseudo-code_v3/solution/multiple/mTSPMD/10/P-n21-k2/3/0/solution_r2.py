import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate distance matrix
def get_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = euclidean(cities[i], cities[j])
    return matrix

distance_matrix = get_distance_matrix(cities)

# Genetic Algorithm Parameters
population_size = 100
num_generations = 1000
mutation_rate = 0.15
elite_size = 10

# Tool functions for GA
def create_route():
    city_list = list(cities.keys())[2:]  # excluding depots
    random.shuffle(city_list)
    return [0] + city_list + [0], [1] + city_list + [1]

def initial_population(pop_size):
    return [create_route() for _ in range(pop_size)]

def route_distance(route):
    return sum([distance_matrix[route[i], route[i+1]] for i in range(len(route)-1)])

def fitness(population):
    return [(route_distance(ind[0]) + route_distance(ind[1]), ind) for ind in population]

def selection(population_ranked, elite_size):
    selection_results = []
    df = [(item[1], item[0]) for item in population_ranked]
    cum_sum = sum([item[1] for item in df])
    prob = [item[1]/cum_sum for item in df]

    for i in range(elite_size):
        selection_results.append(population_ranked[i][1])
    for i in range(len(population_ranked) - elite_size):
        selection_results.append(population_ranked[np.random.choice(range(len(population_ranked)), p=prob)][1])
    return selection_results

def crossover(parent1, parent2):
    # Can improve by using more suitable crossover for permutation problems
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    start_gene = min(geneA, geneB)
    end_gene = max(geneA, geneB)

    childP1 = [parent1[i] for i in range(start_gene, end_gene)]
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child, child[::-1]

def mutate(individual):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def next_generation(current_gen, elite_size):
    ranked_routes = fitness(current_gen)
    selection_results = selection(ranked_routes, elite_size)
    children = []
    for i in range(0, len(selection_results)):
        child = crossover(selection_results[i-1], selection_results[i])
        children.append(child)
    next_generation = [mutate(ind) for ind in children]
    return next_generation

# Genetic Algorithm process
pop = initial_population(population_size)
for i in range(num_generations):
    pop = next_generation(pop, elite_size)

# Get the best route
best_route_index = np.argmin([route_distance(route[0]) + route_distance(route[1]) for route in pop])
best_routes = pop[best_route_index]

robot0_tour = best_routes[0]
robot1_tour = best_routes[1]
robot0_travel_cost = route_distance(robot0_tour)
robot1_travel_cost = route_distance(robot1_tour)
overall_travel_cost = robot0_travel_cost + robot1_travel_cost

# Printing the results
print(f"Robot 0 Tour: {robot0_tour}")
print(f"Robot 0 Total Travel Cost: {robot0_travel_cost}")
print(f"Robot 1 Tour: {robot1_tour}")
print(f"Robot 1 Total Travel Cost: {robot1_travel_cost}")
print(f"Overall Total Travel Cost: {overall_travel_cost}")