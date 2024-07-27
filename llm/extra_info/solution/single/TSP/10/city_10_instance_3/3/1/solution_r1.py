import math
from itertools import permutations

# Coordinates of cities including the depot city at index 0
coordinates = [
    (84, 67),  # Depot city 0
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

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate the total distance of a given tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

# Generate all possible tours starting and ending at the depot, visiting all cities exactly once
def find_shortest_tour():
    cities = list(range(1, len(coordinates)))  # Exclude depot from permutations
    shortest_tour = None
    min_distance = float('inf')

    for perm in permutations(cities):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot
        current_distance = calculate_total_distance(current_tour)

        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour

    return shortest_tour, min_distance

# Solve for the shortest tour
tour, cost = find_shortest_tour()

# Output the shortest tour and its cost
print("Tour:", tour)
print("Total travel cost:", cost)