import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Define the groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities"""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of a given tour"""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour():
    """Find the shortest possible tour visiting one city from each group, using permutations."""
    min_cost = float('inf')
    best_tour = None

    # Iterate over all permutations of choices where one city is taken from each group
    for permutation in permutations([group[0] for group in groups]):
        current_tour = [0]  # start at the depot city
        current_tour.extend(permutation)
        current_tour.append(0)  # return to the depot city
        cost = total_tour_cost(current_tour)
        
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour

    return best_tour, min_cost

# Find the shortest tour and the associated total travel cost
shortest_tour, minimum_cost = find_shortest_tour()
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {minimum_cost}")