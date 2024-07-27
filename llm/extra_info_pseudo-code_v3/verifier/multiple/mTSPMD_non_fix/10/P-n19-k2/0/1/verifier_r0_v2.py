import math

# Coordinates of all cities including two depots
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution data
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1, 0]
robot_0_cost = 194.50
robot_1_tour = [0, 0]
robot_1_cost = 0.00
expected_overall_cost = 194.50

def calculate_distance(city_a, city_b):
    """Calculate the Euclidean distance between two city indices."""
    x1, y1 = cities_coordinates[city_a]
    x2, y2 = cities_coordinates[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_cities_visited_once(tours):
    """Ensure each city except depots are visited exactly once."""
    visit_count = [0] * len(cities_coordinates)
    for tour in tours:
        for city in tour:
            visit_count[city] += 1
    # Check if non-depot cities are visited once and depot cities at least once
    for idx, count in enumerate(visit_count):
        if (idx not in [0, 1] and count != 1) or (0 < idx < 2 and count < 1):
            return False
    return True

def verify_costs(tours, individual_costs):
    """Compare the calculated travel costs against given values."""
    total_calculated_cost = 0
    for i, tour in enumerate(tours):
        tour_cost = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
        if not math.isclose(tour_cost, individual_costs[i], abs_tol=1e-2):
            return False
        total_calculated_cost += tour_cost
    return math.isclose(total_calculated_cost, expected_overall_cost, abs_tol=1e-2)

def test_solution():
    tours = [robot_0_tour, robot_1_tour]
    individual_costs = [robot_0_cost, robot_1_cost]
    if not verify_cities_visited_once(tours):
        return "FAIL: Cities visit constraint failed."
    if not verify_costs(tours, individual_costs):
        return "FAIL: Cost calculation error."
    return "CORRECT"

# Execute the test function
print(test_solution())