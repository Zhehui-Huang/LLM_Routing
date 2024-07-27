import numpy as np
import random

# City coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
depots = list(range(8))
robots = 8
num_cities = len(coordinates)

# Distance matrix computation
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
        else:
            distance_matrix[i, j] = float('inf')

# Genetic Algorithm components
population_size = 100
num_generations = 300

# Initial population: Each depot generates its routes separately
def generate_initial_population():
    population = []
    for _ in range(population_size):
        individual = []
        non_depot_cities = set(range(num_cities)) - set(depots)
        cities_per_robot = len(non_depot_cities) // robots
        
        for depot in depots:
            robot_cities = random.sample(non_depot_cities, cities_per_robot)
            non_depot_cities -= set(robot_cities)
            robot_route = [depot] + robot_cities + [depot]
            individual.append(robot_route)
        
        population.append(individual)
    return population

# Fitness calculation
def calculate_cost(individual):
    cost = 0
    for route in individual:
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i], route[i+1]]
    return cost

# Selection
def tournament_selection(population, scores, k=3):
    selected = []
    for _ in range(population_size):
        contenders_idx = np.random.randint(len(population), size=k)
        contender_costs = [scores[idx] for idx in contenders_idx]
        winner_idx = contenders_idx[np.argmin(contender_costs)]
        selected.append(population[winner_idx])
    return selected

# Crossover
def crossover(parent1, parent2):
    child = []
    for r in range(robots):
        if random.random() < 0.5:
            child.append(parent1[r])
        else:
            child.append(parent2[r])
    return child

# Mutation: swap cities within a route
def mutate(individual, mutation_rate=0.02):
    for route in individual:
        if random.random() < mutation_rate:
            i, j = np.random.randint(1, len(route)-1, 2)  # Avoid the depot
            route[i], route[j] = route[j], route[i]

# Genetic Algorithm execution
population = generate_initial_population()
scores = [calculate_cost(ind) for ind in population]

for generation in range(num_generations):
    selected = tournament_selection(population, scores)
    children = []
    for i in range(0, population_size, 2):
        if i + 1 < population_size:
            child = crossover(selected[i], selected[i+1])
            mutate(child)
            children.append(child)
    population = children
    scores = [calculate_cost(ind) for ind in population]

# Results
best_index = np.argmin(scores)
best_individual = population[best_index]
best_score = scores[best

print("Best Tours:")
for r, route in enumerate(best_individual):
    print(f"Robot {r} Tour: {route}")
    tour_cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    print(f"Travel Cost: {tour_cost}")

print(f"Overall Minimum Cost: {best_score}")