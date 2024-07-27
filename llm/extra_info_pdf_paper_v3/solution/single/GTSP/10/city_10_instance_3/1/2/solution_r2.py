import math
from itertools import permutations

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Compute the total cost of a given tour based on the distance matrix
def calculate_total_distance(tour, dist_matrix):
    total = 0
    for i in range(len(tour) - 1):
        total += dist_matrix[tour[i]][tour[i+1]]
    return total

# Define coordinates of cities including the depot
cities = [
    (84, 67),  # Depot City 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Create a distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Choose one representative per group with a focus on minimal tour
min_total_distance = float('inf')
best_tour = None

# Generate all permutations of choices, one city from each group
for choice_combination in permutations([min(group, key=lambda x: sum(distance_matrix[x][y] for y in group if x != y)) for group in groups]):
    # Create tours from the depot to each choice and back to the depot
    tour = [0] + list(choice_combination) + [0]
    # Calculate the tour cost
    tour_cost = calculate_total_distance(tour, distance_matrix)
    # Check if the found tour has a minimal distance
    if tour_cost < min_total_distance:
        min_total_distance = tour_cost
        best_tour = tour

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_total_distance)