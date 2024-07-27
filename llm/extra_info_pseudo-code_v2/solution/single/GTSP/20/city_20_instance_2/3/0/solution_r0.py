import math
from itertools import permutations

# Define the cities and groups
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
    19: (30, 48)
}

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours by choosing one city from each group
def generate_possible_tours():
    from itertools import product
    return list(product(*groups))

# Evaluate total travel cost of a tour
def evaluate_tour(tour):
    total_cost = 0
    # Start and end at the depot (0)
    current_city = 0
    for city in tour:
        total_cost += euclidean_distance(current_city, city)
        current_city = city
    total_cost += euclidean_distance(current_city, 0)  # Return to depot
    return total_cost

# Find the shortest tour among all possible tours
def find_shortest_tour():
    possible_tours = generate_possible_tours()
    best_tour = None
    min_cost = float('inf')
    
    for tour in possible_tours:
        cost = evaluate_tour(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return [0] + list(best_tour) + [0], min_cost

# Get the best tour and its cost
best_tour, total_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")