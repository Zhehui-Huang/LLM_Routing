import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tours from provided solution
tours = [
    [0, 14, 0], [1, 11, 1], [2, 9, 2], [3, 10, 3],
    [4, 15, 4], [5, 12, 5], [6, 8, 6], [7, 13, 7]
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Verify if all robots return to their starting depots
def check_start_end_points():
    for robot_id, tour in enumerate(tours):
        if tour[0] != robot_id or tour[-1] != robot_id:
            return False
    return True

# Check if all cities are covered exactly once
def check_city_coverage():
    all_cities = set(range(16))
    visited_cities = set()
    for tour in tours:
        visited_cities.update(tour)
    return visited_cities == all_cities

# Verify calculated costs against provided
def check_tour_costs():
    provided_costs = [61.741396161732524, 37.73592452822641, 29.5296461204668, 24.413111231467404,
                      18.439088914585774, 70.3420215802759, 45.34313619501854, 18.439088914585774]
    for i, tour in enumerate(tours):
        total_cost = sum(calculate_distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
        if not math.isclose(total_cost, provided_costs[i], rel_tol=1e-6):
            return False
    return True

# Perform the test
def test_solution():
    if not check_start_end_points():
        return "FAIL: Start/end points error."
    if not check_city_coverage():
        return "FAIL: City coverage error."
    if not check_tour_costs():
        return "FAIL: Cost calculation error."
    return "CORRECT"

# Execute the test
test_result = test_solution()
print(test_result)