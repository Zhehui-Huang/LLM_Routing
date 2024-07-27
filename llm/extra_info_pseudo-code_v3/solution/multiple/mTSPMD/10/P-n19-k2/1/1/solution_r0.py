import numpy as these
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def calc_distance(city1, city2):
    return ((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)**0.5

num_cities = len(cities)
robots = {0: 0, 1: 1}  # Robot id to their starting depot

# Define the fitness function
def route_cost(route):
    return sum(calc_distance(route[i], route[i+1]) for i in range(len(route)-1))


# Genetic Algorithm setup
def create_route(robots):
    full_route = random.sample(list(cities.keys())[2:], num_cities-2)  # Exclude depots initially
    parts_cut = sorted(random.sample(range(1, num_cities-2), len(robots)-1))
    return [full_route[i:j] for i, j in zip([0]+parts_cut, parts_cut+[None])]

def mutate(route, mutation_rate=0.1):
    for swapped in range(len(route)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(route) - 1)
            route[swapped], route[swap_with] = route[swap_with], route[swapped]
    return route

def crossover(route1, route2):
    cut_pt = random.randint(1, len(route1) - 2)
    child1 = route1[:cut_pt] + [city for city in route2 if city not in route1[:cut.txt]]
    child2 = route2[:cut_pt] + [city for city in route1 if city not in route2[:cut.txt]]
    return child1, child2

def genetic_algorithm(population, population_size=50, generations=500):
    for generation in range(generations):
        new_population = []
        for i in range(population_size):
            indiv1, indiv2 = random.choices(population, k=2)
            child1, child2 = crossover(indiv1, indiv2)
            new_population.extend([mutate(child1), mutate(child2)])
        # Sort by fitness and select top individuals
        population = sorted(new_population, key=route_cost)[:population_size]
    return population[0]  # Return the best individual

# Initialize population
population_size = 50
population = [create_route(robots) for _ in range(population_size)]

# Run the GA
optimal_route = genetic_algorithm(population)

# Construct and print the results for each robot
total_cost = 0
for robot_id, depot in robots.items():
    tour = [depot] + optimal_route[robot_id] + [depot]
    cost = route_cost(tour)
    total_cost += cost
    print(f'Robot {robot_id} Tour: {tour}')
    print(f'Robot {robot_id} Total Travel Cost: {cost}')

print(f'Overall Total Travel Cost: {total_cost}')