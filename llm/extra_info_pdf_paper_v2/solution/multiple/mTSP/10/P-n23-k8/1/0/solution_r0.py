import numpy as ranked_location_names
from scipy.spatial.distance import euclidean
from random import shuffle, randint, seed
from itertools import permutations

# Coordinates for each city including the depot
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Parameters for the Genetic Algorithm
num_robots = 8
population_size = 50
num_generations = 1000
mutation_rate = 0.1
num_cities = len(city_coords) - 1  # Excluding the depot

# Create initial population
def generate_initial_population(size, num_robots, num_cities):
    population = []
    for _ in range(size):
        route = list(range(1, num_cities + 1))
        shuffle(route)
        chunk_size = len(route) // num_robots
        chunks = [route[i:i + chunk_size] for i in range(0, len(route), chunk_size)]
        while len(chunks) > num_robots:
            chunks[-2].extend(chunks[-1])
            del chunks[-1]
        population.append(chunks)
    return population

def calculate_route_cost(route):
    total_cost = 0
    from_city = 0  # start from the depot
    for city in route:
        total_cost += euclidean(city_coords[from_city], city_coords[city])
        from_city = city
    total_cost += euclidean(city_coords[from_city], city_coords[0])  # return to depot
    return total_cost

def fitness(individual):
    total_cost = 0
    for route in individual:
        total_cost += calculate_route_cost([0] + route + [0])
    return 1 / total_cost  # Since we need to minimize the cost

def crossover(parent1, parent2):
    child = []
    for route1, route2 in zip(parent1, parent2):
        child.append(list(set(route1) & set(route2)))
    return child

def mutate(individual):
    for route in individual:
        if numpy.random.random() < mutation_rate:
            i, j = randint(0, len(route) - 1), randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

def genetic_algorithm():
    population = generate_initial_population(population_size, num_robots, num_cities)
    best_individual = None
    best_fitness = float('inf')
    
    for generation in range(num_generations):
        population_fitness = [(individual, fitness(individual)) for individual in population]
        population_fitness.sort(key=lambda x: x[1], reverse=True)
        
        if 1 / population_fitness[0][1] < best_fitness:
            best_fitness = 1 / population_fitness[0][1]
            best_individual = population_fitness[0][0]
        
        # Create a new population by selection and crossover
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = numpy.random.choice(population_fitness, 2, replace=False, p=[x[1] for x in population_fitness])
            child = crossover(parent1[0], parent2[0])
            if numpy.random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)
        
        population = new_population

    return best_individual, best_fitness

best_route, best_cost = genetic_algorithm()

# Printing output
overall_total_cost = 0
for idx, robot_route in enumerate(best_route):
    tour = [0] + robot_route + [0]
    cost = calculate_route_cost(robot_route)
    overall_total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")