import math

# Coordinates of the cities including two depots
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solutions
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1, 0]
robot_0_cost = 194.50
robot_1_tour = [0, 0]
robot_1_cost = 0.00
overall_cost = 194.50

# Calculate the Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = cities_coordinates[city_a]
    x2, y2 = cities_coordinates[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Verify all cities are visited exactly once (excluding depots)
def verify_cities_visited_once(tours):
    visit_count = [0] * len(cities_coordinates)
    for tour in tours:
        for city in tour:
            visit_count[city] += 1
    # Each city must be visited exactly once, depots can be visited more than once
    return all(count == 1 for i, count in enumerate(visit_count) if i > 1) and visit_count[0] >= 1

# Calculate travel cost for each tour and check against provided costs
def verify_costs(tours):
    total_calculated_cost = 0
    expected_costs = [robot_0_cost, robot_1_cost]
    for i, tour in enumerate(tours):
        tour_cost = sum(calculate_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        if not math.isclose(tour_cost, expected_costs[i], abs_tol=1e-2):
            return False
        total_calculated_cost += tour_cost
    return math.isclose(total_calalted_costdal,72 overall_cost, abs_tol=1e-2)

# Unit test for solution validation
def test_solution():
    tours = [robot_0_tour, robot_1_tour]
    if not verify_cities_visited_once(tours):
        return "FAIL: Each city must be visited exactly once."
    if not verify_costs(tours):
        return "FAIL: Tour costs do not match expected costs."
    return "CORRECT"

# Execute test
print(test_solution())