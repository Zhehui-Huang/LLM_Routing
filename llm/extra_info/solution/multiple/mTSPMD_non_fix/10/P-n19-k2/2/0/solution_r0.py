import math
import random

# City coordinates with depot cities at the beginning
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Assign cities to depots
def assign_to_closest_depot():
    assignments = {0: [0], 1: [1]}
    for city in range(2, len(cities)):
        if euclidean_distance(city, 0) < euclidean_distance(city, 1):
            assignments[0].append(city)
        else:
            assignments[1].append(city)
    return assignments

# Compute cost of a route
def compute_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(route[i-1], route[i])
    return cost

# Simulated annealing to optimize route
def simulated_annealing(route):
    initial_temp = 100
    final_temp = 1
    alpha = 0.99
    temp = initial_temp
    current_route = route.copy()
    best_route = route.copy()
    current_cost = compute_cost(route)
    best_cost = current_cost
    
    while temp > final_temp:
        for _ in range(100):
            # Swap two cities in the route
            pos1, pos2 = random.sample(range(1, len(route)-1), 2)
            current_route[pos1], current_route[pos2] = current_route[pos2], current_route[pos1]
            new_cost = compute_cost(current_route)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_cost = new_cost
                best_route = current_route.copy()
                best_cost = current_cost
            else:
                # Revert swap
                current_route[pos1], current_route[pos2] = current_route[pos2], current_route[pos1]

        temp *= alpha
    return best_route, best_cost

assignments = assign_to_closest_depot()
results = {}

total_cost = 0
for depot in assignments:
    if len(assignments[depot]) > 1:
        optimized_route, route_cost = simulated_annealing(assignments[depot] + [assignments[depot][0]])
        results[depot] = (optimized_route, route_cost)
        total_cost += route_cost
        print(f"Robot {depot} Tour: {optimized_route}")
        print(f"Robot {depot} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")