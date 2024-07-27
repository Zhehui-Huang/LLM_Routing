import itertools
import math

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Function to compute Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Using a greedy approach to try constructing a biconnected tour
def greedy_tour(cities):
    N = len(cities)
    remaining = set(range(1, N))  # exclude the depot
    tour = [0]  # start at the depot
    last = 0

    while remaining:
        next_city = min(remaining, key=lambda x: distance(last, x))
        tour.append(next_city)
        last = next_city
        remaining.remove(next_city)

    tour.append(0)  # return to the depot
    return tour

# We use a simple greedy algorithm to find an initial tour
tour = greedy_tour(cities)

# Calculate the costs and max distance
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")