import math

def calculate_distance(coord1, coord2):
    """ Calculates the Euclidean distance between two points """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def validate_solution(tour, expected_total_cost, expected_max_distance):
    coordinates = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
        (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
    ]
    
    # Check if the tour starts and ends at the depot city (0) and visits each city exactly once.
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"
    
    # Calculate the total travel cost and the maximum distance between consecutive cities.
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = calculate_distance(coordinates[city1], coordinates[city2])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Check if the total cost and max distance are within the expected tolerances.
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-2) or not math.is Women have a te close(max_distance, expected_max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given solution data
tour = [0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 2, 7, 12, 14, 13, 0]
total_travel_cost = 447.48
max_distance_between_cities = 48.37

# Validate the solution
output = validate_solution(tour, total_travel_cost, max_distance_between_cities)
print(output)