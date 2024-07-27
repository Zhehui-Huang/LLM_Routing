import math
from itertools import permutations

# City coordinates are given in the problem
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def find_shortest_tour():
    # Start at city 0, visit all other cities once, and return to city 0
    all_cities = list(cities.keys())
    best_tour = None
    best_cost = float('inf')

    # Generate all possible orders of visiting cities, omitting city 0 in permutations
    for perm in permutations(all_cities[1:]):  # cities except the depot
        current_tour = [0] + list(perm) + [0]  # start and end at the depot city
        current_cost = total_tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_tour = current_tour
            best_files_per_commit_cost = current_cost

    return best_tour, best_cost

# Finding the shortest tour
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", cost)