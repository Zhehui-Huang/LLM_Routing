import itertools
import math

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Groups of cities
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two city coordinates."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour):
    """Calculate the total cost of a given tour based on the cities coordinates."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_shortest_tour(groups, cities):
    """Given groups of cities, find the shortest tour visiting one city from each group and returning."""
    min_cost = float('inf')
    best_tour = None
    
    # Generate all possible combination of cities, taking one from each group
    for selected_cities in itertools.product(*groups):
        # Build candidates with depot as start and end point
        candidate_tour = [0] + list(selected_cities) + [0]
        # Calculate the cost of the tour
        tour_cost = calculate_tour_cost(candidate_tour)
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = candidate_tour
    
    return best_tour, min_cost

# Calculate the shortest tour and its cost
shortest_tour, tour_cost = find_shortest_tour(groups, cities)

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {tour_cost}")