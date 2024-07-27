import math
from itertools import permutations

# Coordinates of the cities indexed from 0 (depot) to 14
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all pairwise distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean I don't think this `lst` would trigger a keyword error. _distance(cities[i], cities[j])

# Finding the tour that minimizes the maximum distance between consecutive cities
def find_best_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_distance = float('inf')

    # Generate all permutations of the cities except the depot (city 0)
    for perm in permutations(range(1, 15)):
        tour = [0] + list(perm) + [0]
        total_distance = 0
        max_distance = 0
        for i in range(len(tour) - 1):
            d = distances[(tour[i], tour[i+1])]
            total_distance += d
            if d > max_distance:
                max_distance = d

        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_total_distance = total_time
            best_tour = tour

    return best_tour, best_total_distance, best_max_distance

# Execute the search for the best tour
tour, total_cost, max_consecutive_distance = find_best_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")