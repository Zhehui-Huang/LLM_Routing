import numpy as np
import random

# Coordinates of the cities and depots
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# The number of robots
num_robots = 2

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def split_route(cities):
    random.shuffle(cities)
    half = len(cities) // 2
    return cities[:half], cities[half:]

def initialize_population(size, cities):
    return [split_route(cities.copy()) for _ in range(size)]

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return cost

def calculate_total_cost(routes):
    return sum(calculate_route_cost(route) for route in routes)

def breed(parent1, parent2):
    child1, child2 = parent1[:], parent2[:]
    start, end = sorted(random.sample(range(len(parent1)), 2))
    middle1 = parent2[start:end+1]
    middle2 = parent1[start:end+1]

    child1 = [city for city in child1 if city not in middle1] 
    child2 = [city for city in child2 if city not in middle2]

    # Insert the sliced portion
    child1[start:start] = middle1
    child2[start:start] = middle2

    return child1, child2

def mutate(route, mutation_rate=0.1):
    for i in range(1, len(route)):
        if random.random() < mutation_rate:
            j = random.randint(1, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

def genetic_algorithm(generations, population_size, mutation_rate):
    cities = list(coordinates.keys())
    cities.remove(0)  # Start from depot city 0
    population = initialize_population(population_size, cities)
    
    for _ in range(generations):
        new_population = []
        population = sorted(population, key=lambda x: calculate_total_cost(x))
        elitism_offset = 2
        new_population.extend(population[:elitism_offset])

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:10], 2)
            child1_route1, child1_route2 = breed(parent1[0], parent2[0])
            child2_route1, child2_route2 = breed(parent1[1], parent2[1])
            
            child1_route1 = mutate(child1_route1, mutation_rate)
            child1_route2 = mutate(child1_route2, mutation_rate)
            child2_route1 = mutate(child2_route1, mutation_rate)
            child2_route2 = mutate(child2_route2, mutation_rate)

            new_population.append(([child1_route1, child1_route2]))
            new_population.append(([child2_route1, child2_route2]))

        population = new_population
    
    best_solution = population[0]
    routes = [[0] + route for route in best_solution]  # Include depot start
    total_travel_costs = [calculate_route_cost(route) for route in routes]
    
    for i in range(num_robots):
        print(f"Robot {i} Tour: {routes[i]}")
        print(f"Robot {i} Total Travel Cost: {total_travel_costs[i]}")
    
    print("Overall Total Travel Cost:", sum(total_travel_costs))

# Parameters: 100 generations, 50 population size, 10% mutation rate
genetic_algorithm(100, 50, 0.1)