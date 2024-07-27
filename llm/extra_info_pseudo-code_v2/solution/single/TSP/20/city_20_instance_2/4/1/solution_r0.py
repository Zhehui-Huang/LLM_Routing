import math
from itertools import permutations

# City coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48),
}

# Distance calculation
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize the tour starting from depot city 0
def initial_tour(start=0):
    unvisited = list(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    # Nearest neighbor heuristics
    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # Return to the depot
    return tour

# Calculate total travel cost
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate the initial tour and compute its cost
initial_route = initial_tour()
initial_cost = tour_cost(initial_route)

print("Initial Tour:", initial_route)
print("Initial Total Travel Cost:", initial_cost)