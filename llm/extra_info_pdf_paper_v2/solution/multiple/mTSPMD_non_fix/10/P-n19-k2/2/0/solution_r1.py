import numpy as np
import random

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

def create_initial_routes(num_robots, non_depot_cities):
    routes = [[] for _ in range(num_robots)]
    remaining_cities = non_depot_cities[:]
    random.shuffle(remaining_cities)

    # Round-robin assignment of cities to each robot
    for idx, city in enumerate(remaining_cities):
        routes[idx % num_robots].append(city)
    
    return routes

def route_cost(route, depot):
    if not route:
        return 0
    return euclidean_distance(coordinates[depot], coordinates[route[0]]) + \
           sum(euclidean_distance(coordinates[route[i]], coordinates[route[i+1]]) for i in range(len(route) - 1))

def total_cost(routes, depots):
    return sum(route_cost(route, depot) for route, depot in zip(routes, depots))

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

def crossover(route1, route2):
    n = len(route1)
    child = [-1] * n
    
    start, end = sorted(random.sample(range(n), 2))
    child[start:end] = route1[start:end]

    remaining = [city for city in route2 if city not in child]
    pointer = 0

    for i, city in enumerate(child):
        if city == -1:
            child[i] = remaining[pointer]
            pointer += 1

    return child

def ga_solve(depots, num_robots=2, population_size=50, generations=100, mutation_rate=0.01):
    non_depot_cities = list(range(2, len(coordinates)))
    population = [create_initial_routes(num_robots, non_depot_cities) for _ in range(population_size)]

    for _ in range(generations):
        # Evaluate fitness
        population.sort(key=lambda routes: total_cost(routes, depots))
        
        next_generation = population[:2]  # Elitism
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)  # Tournament Selection

            children = []
            for r1, r2 in zip(parent1, parent2):
                if random.random() < 0.7:  # Crossover rate
                    new_route = crossover(r1, r2)
                else:
                    new_route = r1 if route_cost(r1, depots[parent1.index(r1)]) < route_cost(r2, depots[parent2.index(r2)]) else r2
                
                mutate(new_route, mutation_rate)
                children.append(new_route)

            next_generation.append(children)

        population = next_generation

    best_solution = population[0]
    costs = [route_cost(route, depot) for route, depot in zip(best_solution, depots)]
    return best_solution, costs

best_routes, costs = ga_solve([0, 1])
total_overall_cost = sum(costs)

# Outputting the results
for idx, route in enumerate(best_routes):
    tour = [0 if idx == 0 else 1] + route
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")