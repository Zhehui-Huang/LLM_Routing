import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, cities):
    # Extract city coordinates for each city index in the tour
    coordinates = [cities[city] for city in tour]

    # Check if the robot starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, apart from the depot
    visited = set(tour[1:-1])  # skip the first and last entries (depot)
    if len(visited) != len(cities) - 1:
        return "FAIL"

    # Calculate total travel cost as the sum of Euclidean distances between consecutively visited cities
    total_distance = 0
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        total_distance += calculate_euclidean_distance(x1, y1, x2, y2)

    # Capable of returning a rounding corrected distance for test
    expected_distance = 355.524

    # Very minor floating point leniency in python's calculations
    if not (expected_distance - 0.005 <= total_distance <= expected_distance + 0.005):
        return "FAIL"

    return "CORRECT"

# Cities with coordinates
cities = {0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
          5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
          10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)}

# Given solution tour
tour = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]

# Check solution
result = verify_solution(tour, cities)
print(result)