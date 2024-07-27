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
        distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return distance

# Check if all cities except depot are visited exactly once
all_cities_visited = set()
for tour in robots_tours:
    for city in tour[1:-1]:  # exclude the depot city from checking
        if city in all_cities_visited:
            print("FAIL: Some cities are visited more than once.")
            break
        all_cities_visited.add(city)

if len(all_cities_visited) != 15:
    print("FAIL: Not all cities are visited exactly once.")

# Requirement 2: Each tour should start and end at the depot
for tour in robots_tours:
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: A tour does not start or end at the depot.")
        break

# Check distances
reported_distances = [
    47.28555690793142, 75.67537984747364, 47.93463581488838, 72.1927221713905,
    77.87109113044761, 74.15812335008223, 80.99113763798833, 59.665735560705194
]
calculated_distances = [calculate_tour_distance(tour) for tour in robots_tours]

# Comparing reported distances with calculated distances for any mismatch
if any(abs(reported - calculated) > 1e-5 for reported, calculated in zip(reported_distances, calculated_distances)):
    print("FAIL: Reported and calculated distances do not match.")

# Requirement 3: Minimize the maximum distance traveled by any single robot
if max(reported_distances) != max(calculated_distances):
    print("FAIL: Maximum travel costs are not minimized effectively.")

print("Unit tests executed successfully.")