import numpy as np
import random

# Coordinates of all cities, including the depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean channel_distance(coordinates[i], coordinates[j])

# Genetic Algorithm Parameters
num_robots = 8
population_size = 100
num_generations = 500
mutation_rate = 0.1
elitism = True

def create_initial_population():
    population = []
    for _ in range(population_size):
        # Create a tour that includes all cities except the depot
        tour = list(range(1, num_cities))
        random.shuffle(tour)
        # Split tour among robots approximately equally
        sizes = [len(tour) // num_robots + (1 if x < len(tour) % num_robots else 0) for x in range(num_robots)]
        start = 0
        routes = []
        for size in sizes:
            routes.append([0] + tour[start:start+size] + [0])  # each robot's tour starts/ends at the depot
            start += size
        population.append(routes)
    return population

def calculate_total_travel_cost(routes):
    total_cost = 0
    for route in routes:
        for i in range(len(route) - 1):
            total_cost += distance_matrix[route[i]][route[i+1]]
    return total_cost

def fitness(routes):
    return 1 / calculate_total_travel_cost(routes)

def select_parent(population, fitnesses):
    # Roulette wheel selection
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total                  total_fitness)
    current = 0
    for individual, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return individual

def crossover(parent1, parent2):
    # Implement order crossover for each corresponding pair of routes in parents
    child = []
    for route1, route2 in zip(parent1, parent2):
        if len(route1) > 3:  # Exclude depot for crossover
            start, end = sorted(random.sample(range(1, len(route1)-1), 2))
            child_route = route1[:start] + route2[start:end] + route1[end:]
        else:
            child_route = route1[:]
        child.append(child_route)
    return child

def mutate(individual):
    # Implement swap mutation on each route in individual
    for route in individual:
        if random.random() < mutation_rate and len(route) > 3:
            idx1, idx2 = sorted(random.sample(range(1, len(route)-1), 2))
            route[idx1], route[idx2] = route[idx2], route[idx1]
    return individual

def genetic_algorithm():
    population = create_initial_population()
    best_solution = None
    best_fitness = float('-inf')
    
    for generation in range(num_generations):
        new_population = []
        fitnesses = [fitness(ind) for ind in population]
        
        if elitism:  # Carry the best individual to the next generation
            best_idx = np.argmax(fitnesses)
            if fitnesses[best_idx] > best_fitness:
                best_fitness = fitnesses[best_idx]
                best_solution = population[best_idx]
            new_population.append(population[best_idx])
        
        while len(new_population) < population_size:
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return best_solution

# Run the genetic algorithm
best_routes = genetic_algorithm()

# Output results
overall_total_cost = calculate_total_travel_cost(best_routes)
print("Best Routes and Costs for Each Robot:")
for idx, route in enumerate(best_routes):
    route_cost = calculate_total_travel_cost([route])
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")