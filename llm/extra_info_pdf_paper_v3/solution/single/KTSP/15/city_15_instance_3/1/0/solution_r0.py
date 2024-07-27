import math
from itertools import permutations

# Definition of cities - coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79),
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial feasible solution
def initial_solution(depot, include_cities):
    tour = [depot]
    last_city = depot
    remaining_cities = include_cities[:]
    
    while len(tour) < len(include_cities) + 1:
        next_city = min(remaining_cities, key=lambda x: distance(last_city, x))
        remaining_cities.remove(next_city)
        tour.append(next_city)
        last_city = next_city
    
    tour.append(depot)  # return to depot
    return tour

# Calculate total distance of the tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Select cities to include in the tour
selected_cities = [0] + sorted(range(1, 15), key=lambda x: distance(0, x))[:9]

# Obtain initial tour solution
initial_tour = initial_solution(0, selected_cities)
initial_cost = tour_distance(initial_tour)

# Output
print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)