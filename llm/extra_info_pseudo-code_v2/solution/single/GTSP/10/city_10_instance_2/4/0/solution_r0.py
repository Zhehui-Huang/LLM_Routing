import math
import random

# Coordinates of cities
cities = {
    0: (90, 3),   # Depot
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

# City groups
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def distance(c1, c2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour):
    """ Calculate total distance of the tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

def find_shortest_tour(groups, start_city):
    """ Find the shortest possible tour that visits one city from each group """
    permutations = []
    def generate_permutations(current):
        if len(current) == len(groups):
            permutations.append(current)
            return
        for city in groups[len(current)]:
            generate_permutations(current + [city])

    # Generate all permutations each taking one city from each group
    generate_permutations([])
    
    min_tour = None
    min_cost = float('inf')

    # Iterate all permutations to find the one with the minimum cost
    for perm in permutations:
        tour = [start_city] + perm + [start_city]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

    return min_tour, min_cost

# Find the shortest tour starting and ending at the depot (city 0)
tour, total_cost = find_shortest_tour(groups, 0)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")