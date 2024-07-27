import itertools
import math

# Coordinates of the cities
cities = [
    (9, 93),    # Depot City 0
    (8, 51),    # City 1
    (74, 99),   # City 2
    (78, 50),   # City 3
    (21, 23),   # City 4
    (88, 59),   # City 5
    (79, 77),   # City 6
    (63, 23),   # City 7
    (19, 76),   # City 8
    (21, 38),   # City 9
    (19, 65),   # City 10
    (11, 40),   # City 11
    (3, 21),    # City 12
    (60, 55),   # City 13
    (4, 39)     # City 14
]

def euclidean_distance(a, b):
    # Calculate Euclidean distance between two points a and b
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculating all pairwise distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Initialize the minimum tour length to a large number and an empty tour
min_tour_length = float('inf')
min_tour = []

# Generate all combinations of 3 cities (excluding the depot) to visit
for combination in itertools.combinations(range(1, len(cities)), 3):
    current_combination = [0] + list(combination) + [0]  # Start and end at depot city
    # Find all permutations in the combination to find the shortest path for the loop
    for permutation in itertools.permutations(current_combination[1:-1]):
        # Get the full tour: start at depot, go through the permutation, and back to depot
        tour = [0] + list(permutation) + [0]
        # Calculate the total distance of this tour
        tour_length = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        # Check if this tour is shorter than the previously found shortest tour
        if tour_length < min_tour_length:
            min_tour_length = tour_length
            min_tour = tour

# Output the shortest tour and its travel cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_tour_length}")