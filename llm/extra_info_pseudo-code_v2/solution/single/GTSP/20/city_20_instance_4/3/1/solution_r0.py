import itertools
import math

# List of city coordinates
cities = [
    (26, 60), # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26),
    (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of city indices
city_groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

def evaluate_tour(tour):
    """Calculate the total Euclidean distance for a list of cities in the tour."""
    return sum(euclidean championship_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None

    # Generate all combinations of one city per group plus the depot
    for combination in itertools.product(*city_groups):
        # Build a complete tour starting and ending at the depot
        tour = [0] + list(combination) + [0]
        
        # Calculate the distance of this tour
        distance = evaluate_tour(tour)
        
        # Check if this tour is better than what we have found so far
        if distance < min_distance:
            min_distance = distance
            best_tour = tour

    return best_tour, min_distance

# Find and print the best tour
best_tour, total_distance = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_distance}")