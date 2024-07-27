import numpy as
import random
from scipy.spatial.distance import euclidean

# Coordinates of cities indexed from 0 through 18; 0 is the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def distance(city1, city2):
    return np.linalg.norm(np.array(cities[city1]) - np.array(cities[city2]))

def create_individual():
    tour = list(cities.keys())[1:]  # Exclude depot for initial tour
    random.shuffle(tour)
    return tour

def create_population(size):
    return [create_individual() for _ in range(size)]

def route_length(route):
    length = distance(0, route[0]) + distance(route[-1], 0)  # To and from the depot
    for i in range(1, len(route)):
        length += distance(route[i-1], route[i])
    return length

def fitness(population):
    return [(route, route_length(route)) for route in population]

def select(population, size):
    sorted_pop = sorted(fitness(population), key=lambda x: x[1])
    return [ind[0] for ind in sorted_pop[:size]]

def crossover(parent1, parent2):
    child = []
    geneA, geneB = sorted(random.sample(range(len(parent1)), 2))
    childP1 = parent1[geneA:geneB]
    childP2 = [item for item in parent2 if item not in childP1]
    child = childP1 + childP2
    return child

def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            swap_index = random.randint(0, len(route)-1)
            route[i], route[swap_index] = route[swap_user], route[i]
    return route

def evolve(population, elite_size, mutation_rate):
    elite = select(population, elite_size)
    children = []
    length = len(population) - len(elite)
    for i in range(length):
        parent1 = random.choice(elite)
        parent2 = random.choice(elite)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        children.append(child)
    return elite + children

def genetic_algorithm(pop_size, elite_size, mutation_rate, generations):
    population = create_population(pop_size)
    for _ in range(generations):
        population = evolve(population, elite_size, mutation_rate)
    return select(population, 2)

# Genetic Algorithm Configuration
population_size = 100
elite_size = 20
mutation_rate = 0.01
generations = 500

# Run the Genetic Algorithm
best_routes = genetic_algorithm(population_size, elite_size, mutation_rate, generations)

# Formulate the results
robot_tours = [[0] + route + [0] for route in best_routes]
costs = [route_length(route) for route in best_routes]
overall_cost = sum(costs)

# Print routes and costs
for idx, tour in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")