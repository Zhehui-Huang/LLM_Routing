import math

# Given tour and values to be tested
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
max_distance_between_cities = 69.42621983083913

# Coordinates of the cities
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their indices."""
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_second = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, total_travel_cost, max_distance):
    """Verification function to check all requirements of the tour."""
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits each city exactly once (excluding the depot)
    if sorted(tour[:-1]) != sorted(set(tour[:-1])):
        return "FAIL"

    # Requirement 3: Check if calculated total travel cost and the maximum distance are consistent
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        dist = calculate_distance(tour[i], tour[i+1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    if not math.isclose(calculated_total_cost, total_travel_cost, abs_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute the verification
result = verify_tour(tour, total_travel_cost, max_distance_between_cities)
print(result)