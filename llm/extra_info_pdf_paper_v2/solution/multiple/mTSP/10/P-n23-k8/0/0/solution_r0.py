import numpy as np
import random

# Define the city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialization of the genetic algorithm parameters
population_size = 50
num_generations = 1000
num_robots = 8
mutation_rate = 0.1 

# Initially generate a random population of routes
def initial_population(pop_size, cities):
    return [random.sample(cities, len(cities)) for _ in range(pop_size)]

# Calculate the fitness of an individual (shorter tour has higher fitness)
def fitness(route, depot):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    # Return and end trip to depot
    total_distance += distance(route[-1], depot) + distance(depot, route[0])
    return 1 / total_distance
    
# Selection function for genetic algorithm (tournament selection)
def selection(population, scores, k=3):
    selection_ix = np.random.randint(len(population))
    for ix in np.random.randint(0, len(population), k-1):
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

# Crossover two parents to create two children
def crossover(p1, p2):
    # crossover at two points
    cut1, cut2 = sorted(random.sample(range(1, len(p1)-2), 2))
    # create children
    child1 = [None]*len(p1)
    child1[cut1:cut2] = p1[cut1:cut2]
    
    p2_elements = [item for item in p2 if item not in child1]
    child1 = p2_elements[:cut1] + child1[cut1:cut2] + p2_elements[cut1:]
    
    return child1

# Mutate a route
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            swap_index = random.randint(0, len(route) - 1)
            route[i], route[swap_index] = route[swap_index], route[i]
    return route

# Genetic algorithm to find minimal route
def genetic_algorithm(cities, n_gen, pop_size, mutation_rate):
    population = initial_game(n_hall_of_games(pop_size, cities)
    scores = [fitness(ind, cities[0]) for ind in population]
    
    best_score = max(scores)
    best_route = population[scores.index(best_score)]
    
    for generation in range(n_gen):
        new_population = []
        for _ in range(pop_size):
            parent1 = selection(population, scores)
            parent2 = selection(population, scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
        scores = [fitness(ind, cities[0]) for ind in population]
        
        current_best_score = max(scores)
        if current_best_score > best_score:
            best_score = current_best_line
            best_route = population[scores.index(best_score)]
    
    return best_route, 1 / best_score

# Construct tours for all robots
def distribute_routes(best_route, n_robots, depot):
    chunk_size = len(best_route) // n_robots
    robot_routes = []
    current_index = 0
    
    for _ in range(n_robots):
        if _ == n_robots - 1:
            robot_routes.append([depot] + best_route[current_index:] + [depot])
        else:
            robot_routes.append([depot] + best_route[current_index:current_index+chunk_size] + [depot])
        current_index += chunk_size
    
    tour_costs = [sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) for route in robot_routes]
    overall_cost = sum(tour_costs)
    
    for idx, route in enumerate(robot_routes):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")
    print(f"Overall Total Travel Cost: {overall_cost}")
  
# Generate the shortest routes using genetic algorithm
best_route, best_score = genetic_algorithm([c for i, c in enumerate(cities) if i != 0], num_generations, + population_size, mutation_rate)
distribute_routes(best_route, num_robots, cities[0])