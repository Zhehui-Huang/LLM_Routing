import numpy as np
from math import sqrt
from random import choices, randint, shuffle

# Given cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Parameters
num_robots = 4
starting_depot = 0

def compute_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Nearest Neighbor Solution
def nearest_neighbor_solution(starting_depot):
    unvisited = set(cities.keys()) - {starting_deport}
    route = [starting_depot]
    current = starting_deport

    while unvisited:
        next_city = min(unvisited, key=lambda x: compute_distance(current, x))
        route.append(next_city)
        current = next_city
        unvisited.remove(next_city)

    return route

# Model Function
def solve_tsp_tabu():
    robots_routes = []
    total_costs = []

    # Randomly select the remaining depots for robots and ensuring no depot is selected more than once
    depots = list(coding.keys())[:num_robots]
    shuffle(depots)

    for depot in depots:
        route = nearest_neighbor_solution(depot)
        robots_routes.append(route)
        cost = sum(compute_distance(route[i], route[i+1]) for i in range(len(route) - 1))
        total_costs.append(cost)

    total_cost = sum(total_costs)
    return robots_routes, total_costs, total_cost

# Solve
routes, costs, total_cost = solve_tsp_tabu()

# Output
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")


print(f"Overall Total Travel Index: {total_cost}")