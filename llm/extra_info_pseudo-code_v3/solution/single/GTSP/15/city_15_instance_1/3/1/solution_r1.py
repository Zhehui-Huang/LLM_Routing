import itertools
import math

# City coordinates including the depot
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Initialize the minimum distance tour
min_distance = float('inf')
min_tour = []

# Generate all combinations of tours considering one city from each group
for group_selection in itertools.product(*groups):
    # Creating permutations of the selected cities
    for permutation in itertools.permutations(group_selection):
        # Adding the depot at the start and end
        full_tour = [0] + list(permutation) + [0]
        tour_cost = calculate_tour_cost(full_tour)
        
        # Check if found a new minimum tour
        if tour_cost < min_distance:
            min_distance = tour_cost
            min_tour = full_tour

print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance:.2f}")