import numpy as np
from itertools import permutations

# Define the coordinates of the cities
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

# Define function to calculate Euclidean distance between two cities
def distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Calculate all distances between cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(i, j)

# Select 10 cities including the depot
def select_cities(start_city, num_cities):
    unvisited = set(cities.keys())
    visited = [start_city]
    unvisited.remove(start_city)

    current_city = start_city
    while len(visited) < num_max_visits:
        next_city = min(unvisited, key=lambda c: dist_matrix[(current_city, c)])
        visited.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    return visited

num_max_visits = 10
tour = select_cities(0, num_max_visits)

# Find the shortest round tour using the selected cities
def find_shortest_tour(selected_cities):
    min_length = float('inf')
    best_tour = None
    for perm in permutations(selected_cities):
        if perm[0] == 0:  # Ensure it starts with the depot
            length = sum(dist_matrix[(perm[i], perm[i + 1])] for i in range(len(perm) - 1))
            length += dist_matrix[(perm[-1], perm[0])]  # complete the cycle
            if length < min_length:
                min_length = length
                best_tour = perm
    return list(best_tour) + [best_tour[0]], min_length

optimal_tour, total_travel_cost = find_shortest_tour(tour)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_cost)