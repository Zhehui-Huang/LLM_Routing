import itertools
import math

# Define city coordinates including the depot
cities = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Define city groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance"""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def find_shortest_tour(groups, depot=0):
    min_distance = float("inf")
    best_tour = []

    # Generate all combinations of cities where one city is taken from each group
    for combination in itertools.product(*groups):
        # Prepend and append the depot to the tour
        tour = [depot] + list(combination) + [depot]
        # Calculate the distance of the tour
        total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Check if the current distance is less than the minimum found so far
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

    return best_tour, min_distance

# Calculate the shortest tour and its distance
tour, total_distance = find_shortest_tour(groups)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")