import math
import random

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def distance(city1, city2):
    # Calculate Euclidean distance
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initialize_pheromone(level, n):
    return [[level for _ in range(n)] for _ in range(n)]

def choice(probabilities):
    total = sum(probabilities)
    r = random.uniform(0, total)
    upto = 0
    for i, p in enumerate(probabilities):
        if upto + p >= r:
            return i
        upto += p
    assert False, "Should not get here"

def aco_tsp(num_ants, num_cities, num_iterations, alpha, beta, rho, depot):
    pheromone = initialize_pheromone(1.0, num_cities)
    best_route = None
    best_cost = float('inf')

    for _ in range(num_iterations):
        routes = []
        for i in range(num_ants):
            route = [depot]
            unvisited = set(range(num_cities)) - {depot}
            while unvisited:
                current = route[-1]
                probabilities = []
                for next_city in unvisited:
                    if pheromone[current][next_city] == 0:
                        tau = 1e-10
                    else:
                        tau = pheromone[current][next_city]
                    eta = 1 / distance(current, next_city)
                    probabilities.append((tau ** alpha) * (eta ** beta))
                next_city = random.choices(list(unvisited), weights=probabilities, k=1)[0]
                route.append(next_city)
                unvisited.remove(next_city)
            route.append(depot)  # return to depot
            routes.append(route)
        
        for route in routes:
            route_cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
            if route_cost < best_cost:
                best_cost = route_cost
                best_route = route
        
        for route in routes:
            for i in range(len(route)-1):
                pheromone[route[i]][route[i+1]] *= (1-rho)
                pheromone[route[i]][route[i+1]] += 1 / best_cost
        
    return best_route, best_cost

# Set algorithm parameters
num_ants = 5
num_iterations = 200
alpha = 1.0
beta = 2.0
evaporation_rate = 0.2

# Solve separate TSP for each depot
robot0_route, robot0_cost = aco_tsp(num_ants, num_cities, num_iterations, alpha, beta, evaporation_rate, 0)
robot1_route, robot1_cost = aco_tsp(num_ants, num_cities, num_iterations, alpha, beta, evaporation_rate, 1)

print(f'Robot 0 Tour: {robot0_route}')
print(f'Robot 0 Total Travel Cost: {robot0_cost}')
print(f'Robot 1 Tour: {robot1_route}')
print(f'Robot 1 Total Travel Cost: {robot1_cost}')

overall_cost = robot0_cost + robot1_cost
print(f'Overall Total Travel Cost: {overall_cost}')