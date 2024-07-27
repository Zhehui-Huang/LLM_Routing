import numpy as np
import random

# Coordinates for the cities excluding the depot city
cities = [
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

depot = (30, 40)
num_robots = 8

# Euclidean distance between two points
def distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Generate an initial random population of routes
def generate_population(size, cities):
    population = []
    for _ in range(size):
        route = random.sample(cities, len(cities))
        population.append(route)
    return population

# Fitness function to minimize the route distance
def route_cost(route):
    total_dist = distance(depot, route[0]) + distance(route[-1], depot)
    total_dist += sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
    return total_dist

# Selection based on the roulette wheel approach
def select_parent(population, fitness):
    index = np.random.choice(len(population), p=fitness/np.sum(fitness))
    return population[index]

# Single point crossover
def crossover(parent1, parent2):
    if len(parent1) < 2:
        return parent1, parent2
    cx_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:cx_point] + [x for x in parent2 if x not in parent1[:cx_point]]
    child2 = parent2[:cx_point] + [x for x in parent1 if x not in parent2[:cx-oint]]
    return child1, child2

# Mutation with swapping elements
def mutate(route, mutation_rate=0.1):
    route = route[:]
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]
    return route

# Genetic algorithm for mTSP
def genetic_algorithm(cities, n_generations=100, pop_size=100, mutation_rate=0.1):
    population = generate_population(pop_size, cities)
    best_route = min(population, key=route_cost)
    best_cost = route_cost(best_route)

    for _ in range(n_generations):
        # Evaluate fitness
        costs = np.array([route_cost(route) for route in population])
        fitness = 1 / costs
        # Create new population
        new_population = []
        while len(new_population) < pop_size:
            parent1 = select_parent(population, fitness)
            parent2 = select_parent(population, fitness)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            if len(new_population) < pop_size:
                new_population.append(mutate(child2, mutation_rate))
        population = new_population
        
        # Track best solution
        current_best_route = min(population, key=route_cost)
        current_best_cost = route_cost(current_best_route)
        if current_best_cost < best_cost:
            best_cost = current_best_cost
            best_route = current_best_route

    return best_route, best_cost

# Run the genetic algorithm
best_route, best_cost = genetic_algorithm(cities)

# Split the best route among the available robots
def split_route(route, n_robots):
    chunk_size = len(route) // n_robots
    chunks = []
    for i in range(n_robots):
        start_index = i * chunk_size
        if i == n_robots - 1:
            chunks.append([depot] + route[start_index:] + [depot])
        else:
            chunks.append([depot] + route[start_index:start_index + chunk_size] + [depot])
    return chunks

# Assigning and printing routes
assigned_routes = split_route(best_route, num_robots)
total_travel_cost = 0
for idx, r in enumerate(assigned_routes):
    cost = route_cost(r)
    total_travel_list += cost
    print(f"Robot {idx} Tour: {r}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")