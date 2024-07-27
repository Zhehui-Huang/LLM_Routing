import math

# Coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robot tours and costs provided
robot_tours = [
    [0, 0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0]
]

robot_total_cost = [173.0132333806203]

# Check if the robot ends up at the correct depot
def check_start_end_depot(robot_tour):
    return robot_tour[0] == robot_tour[-1]

# Check if all cities are visited exactly once
def check_all_cities_visited_exactly_once(robot_tours):
    all_cities = set(range(16))
    visited_cities = set()
    for tour in robot_tours:
        visited_cities.update(tour)
    visited_cities.remove(0)  # Removing the depot start/end as they are repeated
    return visited_cities == all_cities

# Check travel cost calculation
def calculate_travel_cost(tour):
    cost = 0.0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

# Run the tests
def verify_solution(robot_tours, robot_total_cost):
    if not all(check_start_end_depot(tour) for tour in robot_tours):
        return "FAIL: Not all robots end at their starting depot."

    if not check_all_cities_visited_exactly_once(robot_tours):
        return "FAIL: Not all cities are visited exactly once."

    for tour, expected_cost in zip(robot_tours, robot_total_cost):
        calculated_cost = calculate_travel_cost(tour)
        if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-5):
            return f"FAIL: Cost mismatch. Expected: {expected_cost}, Calculated: {calculated_cost}"

    return "CORRECT"

# Output the verification result
print(verify_solution(robot_tours, robot_total_cost))