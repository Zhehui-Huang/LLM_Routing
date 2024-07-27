from math import sqrt
from itertools import combinations

# Define the cities coordinates including the depot city
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Total number of cities
n = len(cities)

# Step-by-step implementation of the Held-Karp algorithm
def held_karp():
    # Base case: Initialize the cost dictionary with direct paths from the depot
    C = {(frozenset([0, i]), i): (distance(0, i), 0) for i in range(1, n)}
    # Loop through different subset sizes starting with 2 elements (depot and one more)
    for s in range(2, n):
        for subset in combinations(range(1, n), s):
            # Create a set including depot
            subset = frozenset(subset) | frozenset([0])
            # Store the minimum cost to each ending city in the subset
            for k in subset - {0}:
                C[(subset, k)] = min(
                    (C[(subset - frozenset([k]), m)][0] + distance(m, k), m)
                    for m in subset if m != k
                )
    
    # Closing path by returning to depot
    all_visited = frozenset(range(n))
    min_cost, parent = min(
        (C[(all_visited, k)][0] + distance(k, 0), k) for k in range(1, n)
    )

    # Backtrack to get the tour
    tour = [0]
    for _ in range(n - 1):
        tour.append(parent)
        new_subset = all_visited - frozenset([parent])
        _, parent = C[(all_visited, parent)]
        all_visited = new_subset

    # Complete tour by returning to depot
    tour.append(0)
    return tour, min_cost

# Find the tour and the cost
tour, total_cost = held_karp()

# Printing tour and total cost outputs
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))