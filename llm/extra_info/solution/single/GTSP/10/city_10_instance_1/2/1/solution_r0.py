import itertools
import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Grouping of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of one city from each group
def possible_routes():
    for cities_in_groups in itertools.product(*groups):
        yield [0] + list(cities_in_groups) + [0]

# Function to calculate the total cost of a route
def total_cost(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Find the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    for route in possible_routes():
        cost = total_cost(route)
        if cost < min_cost:
            min_cost = cost
            min_tour = route
    
    return min_tour, min_cost

# Get the shortest tour and its cost
shortest_tour, tour_cost = find_shortest_tour()

# Output the result
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {tour_cost:.2f}")