import numpy as np
from math import sqrt

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4

# Compute Euclidean distance between two city indices
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Assigning cities to robots using a simple nearest neighbors algorithm
def nearest_neighbor_solution(depot, unvisited_cities):
    tour = [depot]
    cost = 0
    current_city = depot

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: euclidean_distance(current_city, x))
        cost += euclidean_distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(next_city)

    return tour, cost

# Main function to calculate routes and costs
def solve_tsp():
    all_cities = set(cities.keys())
    depot_cities = [0]  # Starting depots, more can be added if needed
    tours = []
    overall_cost = 0
    costs = []

    unvisited_cities = all_cities - set(depot_cities)
    for depot in depot_cities:
        if unvisited_cities:
            tour, cost = nearest_neighbor_solution(depot, unvisited_cities)
            tours.append(tour)
            costs.append(cost)
            overall_cost += cost

    return tours, costs, overall_cost

# Execute the TSP Solver
tours, costs, overall_cost = solve_tsp()

# Printing results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {overall_cost}")