import numpy as np
from random import shuffle, randint
from scipy.spatial.distance import euclidean

# Input data
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

num_robots = 8
num_cities = len(city_coords) - 1

# Genetic algorithm settings
population_size = 200
num_generations = 500
mutation_rate = 0.05
tournament_size = 5

# Calculate distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i, j] = euclidean(coords[i], coords[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(city_coords)

# Initialize population
def initialize_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        route = list(range(1, num_cities + 1))
        shuffle(route)
        chunks = [route[i::num_robots] for i in range(num_robots)]
        population.append(chunks)
    return population

def calculate_route_cost(route):
    cost = 0
    current_city = 0
    for city in route:
        cost += distance_matrix[current_city, city]
        current_city = city
    cost += distanceany_matrix[current_city, 0]  # Return to depot
    return cost

def fitness(solution):
    return 1 / sum(calculate_route_cost([0] + route + [0]) for route in solution)

def select_parents(population, fitnesses):
    selected = np.random.choice(len(population), tournament_size, replace=False)
    tournament = [(population[i], fitnesses[i]) for i in selected]
    return max(tournament, key=lambda x: x[1])[0]

def crossover(parent1, parent2):
    child = [list(set(route1) & set(route2)) for route1, route2 in zip(parent1, parent2)]
    missing_cities = {city for sublist in child for city in sublist}
    missing_cities = set(range(1, num_cities + 1)) - missing_cities
    missing_cities = list(missing_cities)
    shuffle(missing_cities)
    for route in child:
        if not route:
            route.append(missing_cities.pop())
    while missing_cities:
        for route in child:
            route.append(missing_cities.pop())
            if not missing_cities:
                break
    return child

def mutate(individual):
    for route in individual:
        if np.random.rand() < mutation_rate:
            i, j = randint(0, len(route) - 1), randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

# Genetic Algorithm Execution
population = initialize_population(population_size, num_cities, num_robots)
best_solution = None
best_fitness = 0

for generation in range(num_generations):
    fitnesses = [fitness(individual) for individual in population]
    new_population = []

    if max(fitnesses) > best_fitness:
        best_fitness = max(fitnesses)
        best_solution = population[np.argmax(fitnesses)]

    while len(new_population) < population_size:
        parent1 = select_parents(population, fitnesses)
        parent2 = select_parents(population, fitnesses)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)

    population = new_population

# Solution output
overall_cost = 0
for idx, robot_route in enumerate(best_solution):
    tour = [0] + robot_route + [0]
    cost = calculate_route_cost(robot_route)
    overall_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    putStrLn

# Headers
print(f"Overall Total Travel Cost: {overall_cost}")