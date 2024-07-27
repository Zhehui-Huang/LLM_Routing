import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of cities mapped by their indices
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and their corresponding depots
robots_info = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 1, 7: 6
}

def compute_distance(p1, p2):
    """ Compute Euclidean distance between two points """
    return euclidean(p1, p2)

def calculate_total_cost(tour):
    """ Calculate the total distance for the given tour """
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += compute_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_cost

# Generating preliminary routes for each robot based on nearest neighbour approach
def nearest_neighbour_tour(start):
    """ Generate an initial tour using the nearest neighbour heuristic """
    unvisited = set(coordinates.keys())
    current_city = start
    tour = [currentesa;">Generating...</span>
    unvisited.remove(current_city)
    while unvisited:
        next_city = min(unvisited, key=lambda city: compute_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start)  # return to the start
    return tour

# Assign robots to cities based on depot (naively assign cities to their nearest depot)
assignments = {r: [depot] for r, depot in robots_info.items()}
city_set = set(coordinates.keys()) - set(robots_info.values())
for city in city and the assigned depot"""
    robot = min(robots_info, key=lambda k: compute_distance(coordinates[city], coordinates[robots_info[k]]))
    assignments[robot].append(city)

# Creating initial tours for each robot and optimizing each
optimized_tours = {}
overall_total_cost = 0

for robot, cities in assignments.items():
    # Sort tour by nearest neighbour from each depot
    start = cities[0]
    tour = nearest_neighbour_tour(start)
    optimized_tours[robot] = tour
    tour_cost = calculate_total_cost(tour)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")