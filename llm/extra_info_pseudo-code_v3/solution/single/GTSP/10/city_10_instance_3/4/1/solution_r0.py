import itertools
from math import sqrt

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to calculate total travel cost of a tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Function to find the shortest tour
def find_shortest_tour(groups):
    # Create all combinations of cities, picking one from each group
    all_combinations = itertools.product(*groups)
    best_tour = None
    min_cost = float('inf')
    
    # Iterate through each combination to form a tour and calculate its cost
    for combination in all_combinations:
        tour = [0] + list(combination) + [0]
        cost = calculate_total_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Find and display the shortest tour
best_tour, min_cost = find_shortest_tour(groups)
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))