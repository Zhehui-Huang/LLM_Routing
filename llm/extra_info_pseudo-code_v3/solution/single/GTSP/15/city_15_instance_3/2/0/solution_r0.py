import itertools
import math

# City coordinates
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

# City groups as lists of city indices
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def total_trip_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    # Generate all combinations of cities, one from each group
    all_possible_tours = itertools.product(*city_groups)
    
    # Initialize the shortest tour and its cost arbitrarily high
    shortest_tour = None
    min_cost = float('inf')
    
    # Check each possible tour beginning and ending with the depot
    for tour in all_possible_tours:
        full_tour = [0] + list(tour) + [0]
        cost = total_trip_distance(full_tour)
        if cost < min_cost:
            min_cost = cost
            shortest_tourn = full_tour

    return shortest_tour, min_cost

# Finding the optimal tour
optimal_tour, optimal_cost = find_shortest_tour()

# Outputting the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)