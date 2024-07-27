import numpy as np
import random

# Coordinates of each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Euclidean distance function
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Parameters of ACO
antnum = 50
cyclenum = 100
inittrail = 1.0
alpha = 1.0
beta = 2.0
rho = 0.5

# Number of cities
num_cities = len(coordinates)

# Assign starting depots
depots = [0, 1]

# Initialize pheromone levels
pheromone = np.ones((num_cities, num_cities)) * inittrail

# Initialize heuristic information (inverse of distance)
heuristic = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            heuristic[i][j] = 1.0 / distance(i, j)

def get_route(depot):
    route = [depot]
    visited = set(route)
    current_city = depot
    
    while len(visited) < num_cities:
        probabilities = []
        for city in range(num_cities):
            if city not in visited:
                tau = pheromone[current_city][city] ** alpha
                eta = heuristic[current_city][city] ** beta
                probabilities.append(tau * eta)
            else:
                probabilities.append(0)
        
        probabilities = np.array(probabilities)
        probabilities /= probabilities.sum()
        next_city = np.random.choice(range(num_cities), p=probabilities)
        route.append(next_city)
        visited.add(next_city)
        current_city = next_city
        
        if len(visited) == num_cities:
            # Return to depot
            route.append(depot)
    
    return route

def evaluate_route(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance(route[i], route[i+1])
    return total_cost

for cycle in range(cyclenum):
    routes = []
    route_costs = []
    for ant in range(antnum):
        depot = random.choice(depots)
        route = get_route(depot)
        cost = evaluate_route(route)
        routes.append(route)
        route_costs.append(cost)
    
    # Update pheromone (evaporation)
    pheromone *= (1 - rho)
    
    # Pheromone addition
    for i, route in enumerate(routes):
        for j in range(len(route) - 1):
            start, end = route[j], route[j + 1]
            pheromone[start][end] += 1.0 / route_costs[i]

# Pick the best solution after all cycles
best_cost = float('inf')
best_route_index = -1
for i, cost in enumerate(route_costs):
    if cost < best_cost:
        best_cost = cost
        best_partial_route = routes[i]

# Break best_route into two tours starting from each depot
final_routes = {0: [], 1: []}
for i in depots:
    index = best_partial_route.index(i)
    next_index = best_partial_route.index(i, index + 1) + 1
    final_routes[i] = best_partial_route[index:next_index]

print(f"Robot 0 Tour: {final_routes[0]}")
print(f"Robot 0 Total Travel Cost: {evaluate_route(final_routes[0])}")
print(f"Robot 1 Tour: {final_routes[1]}")
print(f"Robot 1 Total Travel Cost: {evaluate_route(final_routes[1])}")
overall_total_cost = evaluate_route(final_routes[0]) + evaluate_route(final_routes[1])
print(f"Overall Total Travel Cost: {overall_total_cost}")