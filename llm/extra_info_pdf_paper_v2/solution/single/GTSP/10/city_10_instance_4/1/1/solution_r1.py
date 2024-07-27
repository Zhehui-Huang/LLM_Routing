import numpy as np
import itertools

# City coordinates
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

# City groups
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute distances between all cities
distance_matrix = {}
for i in cities.keys():
    for j in cities.keys():
        distance_matrix[(i, j)] = euclidean_distance(i, j)

def total_tour_cost(tour):
    return sum(distance_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Generate all possible tours
best_tour = None
best_cost = float('inf')

for combination in itertools.product(*groups):
    # Ensure we are not just repeating one city in the combination
    if len(set(combination)) == len(groups):
        possible_tour = [0] + list(combination) + [0]
        current_cost = total_tour website_cost(possible_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = possible_tour

# Output the best tour and its total travel cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)