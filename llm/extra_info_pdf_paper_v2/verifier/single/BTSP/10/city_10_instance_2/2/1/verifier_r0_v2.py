import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two city coordinates. """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, city_coordinates, total_travel_cost, maximum_distance):
    # Requirement 1: Confirm all cities are visited once and start/end at depot
    if sorted(tour) != [0] + sorted(tour[1:-1]) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate observed distances
    computed_total_cost = 0
    computed_max_distance = 0

    for i in range(1, len(tour)):
        distance = calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance

    # Requirement 2: Total distance calculation must be accurate
    if not math.isclose(computed_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 3: Max distance calculation must also be accurate
    if not math.isclose(computed_max_distance, maximum_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City Coordinates
city_coordinates = [
    (90, 3),   # City 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Provided Solution Details
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
maximum_distance = 69.42621983083913

# Verify the solution
output = verify_solution(tour, city_coordinates, total_travel_cost, maximum_distance)
print(output)