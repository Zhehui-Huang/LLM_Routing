import numpy as np
import random

# Coordinates of the cities, including the depot city (index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

# Number of robots
num_robots = 4

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the path cost
def path_cost(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path)-1))

# Random path generation for initial population
def generate_initial_population(population_size, num_cities):
    population = []
    for _ in range(population_size):
        path = list(range(1, num_cities + 1))
        random.shuffle(path)
        paths = []
        sizes = [num_cities // num_robots] * num_robots
        for i in range(num_cities % num_robots):
            sizes[i] += 1
        start = 0
        for size in sizes:
            end = start + size
            paths.append([0] + path[start:end] + [0])
            start = end
        population.append(paths)
    return population

# Genetic algorithm main process
def genetic_algorithm(coordinates, num_generations=400, population_size=50, mutation_rate=0.01):
    num_cities = len(coordinates) - 1
    population = generate_initial_population(population_size, num_cities)
    
    for generation in range(num_generations):
        # Evaluate all individuals in the population
        population_costs = [(individual, sum(path_cost(path) for path in individual)) for individual in population]
        population_costs.sort(key=lambda x: x[1])
        
        # Select the best solutions to survive
        survival_size = population_size // 2
        population = [tours for tours, cost in population_costs[:survival_size]]
        
        # Crossover and mutation to generate new individuals
        new_generation = population.copy()
        while len(new_generation) < population_size:
            parent1, parent2 = random.sample(population, 2)
            # Simple crossover and mutation for demonstration
            child = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
            if random.random() < mutation_rate:
                for tour in child:
                    i, j = random.sample(range(1, len(tour)-1), 2)
                    tour[i], tour[j] = tour[j], tour[i]
            new_generation.append(child)
        
        population = new_generation
    
    best_solution = population[0]
    best_cost = sum(path_cost(path) for path in best_solution)
    return best_solution, best_cost

# Solve the problem using the genetic algorithm
best_solution, best_cost = genetic_algorithm(coordinates)

# Display the results
for i, tour in enumerate(best_solution):
    tour_cost = path_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_m_cost:.2f}")

print(f"Overall Total Travel Cost: {best_cost:.2f}")