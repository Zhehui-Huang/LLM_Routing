import math
from itertools import permutations, product

# Define the positions of the cities
positions = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Grouping of the cities
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Evaluate the total distance of a tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Find the shortest tour visiting one city from each group
def find_best_tour():
    shortest_distance = float('inf')
    best_tour = None
    # Iterate over all combinations of one city from each group
    for selection in product(*city_groups):
        # Check each permutation of the selected cities
        for perm in permutations(selection):
            tour = [0] + list(perm) + [0]  # Starting and ending at depot
            dist = evaluate_tour(tour)
            if dist < shortest_distance:
                shortest_distance = dist
                best_tour = tour
    return best_tour, shortest_distance

# Main execution to solve the problem
best_tour, shortest_distance = find_best_tour()

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(shortest_distance, 2))