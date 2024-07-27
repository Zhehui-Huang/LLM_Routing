import itertools
import math

# Coordinates of the cities; Index matches city number
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Groups of cities based on given data
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute distances between all possible pairs of cities
distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

def calculate_total_distance(tour):
    """Calculate the total distance covered by the robot on a given tour."""
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += distances[(tour[i-1], tour[i])]
    total_distance += distances[(tour[-1], tour[0])]  # Return to depot city
    return total_distance

def find_shortest_tour():
    """Find the shortest possible tour visiting one city from each group."""
    all_possible_city_combinations = itertools.product(*city_groups)
    shortest_tour = None
    min_distance = float('inf')

    for combination in all_possible_city_combinations:
        complete_tour = [0] + list(combination) + [0]  # Including the depot city (start and end)
        current_distance = calculate_total_distance(complete_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = complete_tour

    return shortest_tour, min_decode by 1

# Calculate the shortest tour and its cost
shortest_tour, min_distance = find_shortest_tour()

print("Tour:", shortest_tour)
print("Total travel cost:", min_distance)