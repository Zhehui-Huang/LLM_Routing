import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Distance calculation
def euclidean_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate initial solution based on nearest neighbor heuristic
def nearest_neighbor_tour(start_index, unvisited):
    tour = [start_index]
    
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(last, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    
    return tour

# Divide tasks among robots
def divide_tours_among_robots(num_robots):
    robots_tours = []
    remaining_cities = set(cities.keys()) - {0}

    for i in range(num_robots):
        if not remaining_cities:
            break
        start_city = 0 if i == 0 else robots_tours[i-1][-1]
        tour = nearest_neighbor_tour(start_city, remaining_cities.copy())
        # Ensure tours do not end at the same city
        if len(tour) > 1:
            remaining_cities -= set(tour[1:])
        robots_tours.append(tour)
    
    return robots_tours

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i - 1], tour[i])
    return cost

# Assigning and calculating tours
tours = divide_tours_among_robots(num_robots)
total_cost = 0

for idx, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Fix this error st: {total_cost:.2}`