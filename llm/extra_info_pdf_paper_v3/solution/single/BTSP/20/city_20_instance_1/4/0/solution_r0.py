import math
from itertools import permutations

# Coordinates of the depot and cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all necessary distances
N = len(cities)
distances = [[euclidean_distance(i, j) for j in range(N)] for i in range(N)]

# Function to calculate maximum distance and total cost of a route
def assess_route(route):
    max_leg = max(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    return total_cost, max_leg

# Heuristic: Greedy approach to minimize the maximum leg distance
def greedy_min_max_leg(start):
    unvisited = set(cities.keys() - {start})
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(start)  # Complete the tour by going back to depot
    return tour

# Find a tour starting from the depot city 0
tour = greedy_min_max_leg(0)
total_cost, max_distance = assess_route(tour)

# Output the required results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")