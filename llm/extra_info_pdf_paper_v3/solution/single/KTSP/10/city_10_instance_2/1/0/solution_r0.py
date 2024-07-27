import numpy as np
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Implementing a greedy randomized k-subset selector
def select_random_k_subset(k, excluding):
    available_cities = list(set(cities.keys()) - {excluding})
    selected = [excluding]
    selected += list(np.random.choice(available_cities, k-1, replace=False))
    selected.append(excluding)
    return selected

# Implementing the 2-opt optimization heuristic for a given route
def optimize_route(route):
    best_route = route
    improve = True
    while improve:
        improve = False
        for i in range(1, len(best_route) - 2):
            for j in range(i+2, len(best_route)):
                if j-i == 1: continue  # skip adjacent edges
                new_route = best_route[:]
                new_route[i:j] = best_route[j-1:i-1:-1] # reverse part of the route
                if route_cost(new_route) < route_cost(best_route):
                    best_route = new_route
                    improve = True
        route = best_route
    return best_route

def route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(route[i], route[i + 1])
    return cost

# Main algorithm using multi-start heuristic approach
def solve_k_tsp(k=6):
    num_trials = 1000
    best_route = None
    min_cost = float('inf')
    
    for _ in range(num_trials):
        initial_route = select_random_k_subset(k, 0)
        optimized_route = optimize_route(initial_route)
        current_cost = route_cost(optimized_route)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = optimized_route
    
    return best_route, min_cost

# Solve the problem
best_tour, total_cost = solve_k_tsp(6)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")