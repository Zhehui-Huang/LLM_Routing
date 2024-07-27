import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities_coordinates = {
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

    # [Requirement 1] The robot must start and end its route at the depot city (city index 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city must be visited exactly once by the robot, except for the depot city which must be visited twice.
    if set(tour) != set(cities_coordinates.keys()) or tour.count(0) != 2:
        return "FAIL"

    # Calculate the actual total travel cost and maximum distance for verification
    actual_total_cost = 0
    actual_max_distance = 0

    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        x1, y1 = cities_coordinates[city_a]
        x2, y2 = cities_coordinates[city_b]
        distance = calculate_distance(x1, y1, x2, y2)
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance

    # Comparing calculated costs and distances with the provided ones
    if not math.isclose(actual_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(actual_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the solution given
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_cost = 418.32344417340323
max_distance = 69.42621983083913

result = verify_solution(tour, total_cost, max_distance)
print(result)