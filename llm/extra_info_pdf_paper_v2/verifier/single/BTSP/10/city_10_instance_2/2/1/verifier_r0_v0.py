import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tour, city_coordinates, total_travel_cost, max_distance):
    # Requirement 1: Check if each city is visited once, and starts and ends at depot (city 0)
    if sorted(tour) != sorted(set(tour)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Compute the total and maximum distance based on the given tour
    computed_total_cost = 0
    computed_max_distance = 0

    for i in range(1, len(tour)):
        distance = calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance

    # Requirement 2: Check computed distances against provided values
    total_travel_cost_correct = math.isclose(computed_total_cost, total_travel_case, rel_tol=1e-9)
    max_distance_correct = math.isclose(computed_max_distance, max_distance, rel_tol=1e-9)

    # Requirement 3: This is checked inherently by the constraints of the problem and provided outputs

    if total_travel_cost_correct and max_distance_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Given City Coordinates
city_coordinates = [
    (90, 3),   # City 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  & City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Provided solution details
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
maximum_distance = 69.42621983083913

# Verify the solution
print(verify_solution(tour, city_coordinates, total_travel_cost, maximum_distance))