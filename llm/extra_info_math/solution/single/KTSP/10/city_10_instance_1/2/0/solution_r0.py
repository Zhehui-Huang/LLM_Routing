import math
from itertools import combinations

# City coordinates indexed by city number
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calculate_tour_cost(tour):
    """ Calculate the total tour cost """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None

    # Generate all combinations of 4 cities (excluding depot) + depot
    for cities in combinations(range(1, 10), 4):
        cities = (0,) + cities  # Add the depot city at the start

        # Generate all permutations to form a tour that starts and ends at the depot
        for perm in permutations(cities):
            tour = list(perm) + [0]  # Adding depot again to the end
            cost = calculate_tour_cost(tour)

            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

from itertools import permutations

# Find and print the best tour with its total cost
best_tour, min_cost = find_shortest_tour()
print("Tour:", best_tour)
print("Total travel cost:", min_cost)