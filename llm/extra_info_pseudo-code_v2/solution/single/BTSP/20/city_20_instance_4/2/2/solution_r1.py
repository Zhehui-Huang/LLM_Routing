import math
from itertools import permutations

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Find a tour using brute force approach
def find_tour():
    n = len(cities)
    min_max_dist = float('inf')
    best_tour = []
    all_tours = permutations(range(1, n))  # Exclude the depot city for permutation

    for tour in all_tours:
        # Complete the tour by adding depot city at start and end
        full_tour = [0] + list(tour) + [0]
        max_dist_in_tour = max(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
        
        if max_dist_in_tour < min_max_dist:
            min_max_dist = max_dist_in_tour
            best_tour = full_tour

    # Calculate total travel cost
    total_travel_cost = sum(distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1))

    return best_tour, total_travel_cost, min_max_dist

# Invoke the function and get the solution
tour, total_cost, max_dist = find_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")