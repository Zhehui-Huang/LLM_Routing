import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def calculate_distance(c1, c2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_tour_cost(tour):
    """ Calculate the total tour cost based on the tour """
    cost = 0
    for i in range(1, len(tour)):
        cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

# Generating all possible tours that start and end at the depot, visiting exactly 5 other cities (total 6)
min_cost = float('inf')
best_tour = None

# Consider all combinations of visiting 5 cities from cities excluding the depot (indices: 1-14)
for perm in permutations([i for i in range(1, 15)], 5):  # Generate permutations of 5 cities
    tour = (0,) + perm + (0,)  # Append the depot city at the start and the end
    cost = total_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Outputs
print("Tour:", list(best_tour))
print("Total travel cost:", min_cost)