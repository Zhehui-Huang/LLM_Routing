import itertools
import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Compute distances between cities
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Precompute the distances
distances = [[euclidean_distance(i, j) for j in range(len(cities))] for i in range(len(cities))]

# Generate all possible tours
def all_possible_tours():
    for combination in itertools.product(*groups):
        # Always include the depot city (0) in the tour
        yield (0,) + combination + (0,)

# Calculate the cost of a tour
def tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Find the tour with the minimum cost
def find_minimum_tour():
    min_cost = float('inf')
    min_tour = None
    for tour in all_possible_tours():
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    return min_tour, min_cost

# Run the search for the minimum tour
min_tour, min_cost = find_minimum_tour()

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")