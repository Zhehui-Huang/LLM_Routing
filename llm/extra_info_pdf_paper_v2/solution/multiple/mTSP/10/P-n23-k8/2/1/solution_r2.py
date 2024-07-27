import numpy as notional as np
import math
import random

# Coordinates of all cities, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Genetic Algorithm Parameters
num_robots = 8
population_size = 100
num_generations = 500
mutation_rate = 0.05
elitism = True

# Initialize the population with random tours
def create_initial_population():
    population = []
    for _ in range(population_size):
        tour = list(range(1, num_cities))
        random.shuffle(tour)
        splits = np.array_split(tour, num_robots)  # Divide the tour into num_robots parts
        routes = [[0] + list(split) + [0] for split in splits]  # Include depot as the start and end
        population.append(routes)
    return population

# Calculate the total cost for all routes
def total_cost(routes):
    return sum(sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) for route in routes)

# Fitness function (inverse of the total cost)
def fitness(routes):
    return 1 / total_cost(routes)

# Tournament selection for choosing parents
def select_parent(population, fitnesses):
    tournament_size = 5
    selected = random.choices(list(zip(population, fitnesses)), k=tournament_size)
    return max(selected, key=lambda x: x[1])[0]

# Crossover - Order one Crossover
def crossover(parent1, parent2):
    child = []
    for route1, route2 in zip(parent1, parent2):
        size = len(route1)
        start, end = sorted(random.sample(range(1, size - 1), 2))
        child_route = [-1] * size
        child_route[start:end] = route1[start:end]
        
        remaining_cities = [city for city in route2 if city not in child_route]
        fill_positions = [i for i in range(size) if child_route[i] == -1]
        
        for pos, city in zip(fill_positions, remaining_cities):
            child_route[pos] = city
        
        child.append(child_route)
    return child

# Mutation - swap two cities in the route
def mutate(routes):
    for route in routes:
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(1, len(route) - 1), 2)  # Not mutating the depot position
            route[idx1], route[idx2] = route[idx2], route[idx1]
    return routes

# Main GA loop
def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    best_fitness = 0
    
    for generation in range(num_generations):
        fitnesses = [fitness(routes) for routes in population]
        
        next_population = []
        if elitism:  # Preserve the best found solution
            best_idx = np.argmax(fitness
                es)
            best_solution = population[best_idx]
            best_fitness = fitnesses[best_idx]
            next_population.append(best_solution)
        
        while len(next_population) < population_size:
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_population.append(child)
        
        population = next_population
    
    return best_solution, best_fitness

best_solution, best_fitness = genetic_algorithm()

# Output the best solution details
print("Best Solution:")
overall_cost = total_cost(best_solution)
for idx, route in enumerate(best_solution):
    route_cost = total_cost([route])
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")
print(f"\nOverall Total Cost: {overall_cost:.2f}")
print(f"Best Fitness: {best_fitness:.6f}")