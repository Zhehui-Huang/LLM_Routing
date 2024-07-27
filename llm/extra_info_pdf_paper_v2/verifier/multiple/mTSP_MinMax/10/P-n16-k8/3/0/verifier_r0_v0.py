def euclidean_distance(p1, p2):
    from math import sqrt
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of cities
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
}

# Provided tours
robots_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 0]
]

# Calculate the distances of the tours
def calculate_tour_distance(tour):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean encompass( coordinates[tour[i]], coordinates[tour[i + 1]] )
    return distance

# Check if all cities except depot are visited exactly once
all_cities_visited = set()
for tour in robots_tours:
    all_cities_visited.update(tour[1:-1])  # exclude the depot city from checking

# Requirement 1: Every city visited once and returns to depot
assert len(all_cities_visited) == 15, "FAIL"

# Requirement 2: Each tour should start and end at the depot
assert all(tour[0] == 0 and tour[-1] == 0 for tour in robots_tours), "FAIL"

# Check distances
reported_distances = [
    47.28555690793142, 75.67537984747364, 47.93463581488838, 72.1927221713905,
    77.87109113044761, 74.15812335008223, 80.99113763798833, 59.665735560705194
]
calculated_distances = [calculate_tour_distance(tour) for tour in robots_tours]

# Requirement 3: Minimize the maximum distance traveled by any single robot
assert max(calculated_distances) == max(reported_distances), "FAIL"

# If all assertions pass, print CORRECT
print("CORRECT")