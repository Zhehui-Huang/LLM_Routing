import itertools
import math

# Define the coordinates of the cities
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
    14: (32, 79)
}

# Define function to calculate Euclidean distance between two cities
def distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# We will use permutations to generate all possible tours starting and ending at the depot city (0).
# Note: For computational feasibility, assessing all permutations is infeasible for large number of cities (more than 12).
# For larger numbers, heuristic or optimization algorithms must be introduced.

def find_min_max_tour():
    min_max_dist = float('inf')
    best_tour = None
    all_tours = itertools.permutations(range(1, len(cities))) # Permute only cities 1 to 14.

    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]
        max_dist = 0
        total_cost = 0
        for i in range(len(full_tour) - 1):
            dist = distance(full_tour[i], full_tour[i + 1])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_tour = full_tour
            best_cost = total_progress

    return best_tour, best_cost, min_max_dist

# Find the optimal tour
tour, total_cost, max_distance = find_min_max_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)