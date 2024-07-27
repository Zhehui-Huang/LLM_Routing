import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robot_tours, total_costs, coordinates):
    # Extract tours and total travel cost details
    robot_0_tour = robot_tours[0]
    robot_0_cost = total_costs[0]
    robot_1_tour = robot_tours[1]
    robot_1_cost = total_costs[1]
    overall_cost = sum(total_costs)

    # Verify correct starting and ending depots for each robot
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL: Robot 0 does not start and end at depot 0."
    
    if robot_1_tour and (robot_1_tour[0] != 1 or robot_1_tour[-1] != 1):
        return "FAIL: Robot 1 does not start and end at depot 1."
    
    # Ensuring all cities are visited exactly once
    all_cities_visited = sorted(robot_0_tour[1:-1] + robot_1_tour[1:-1])
    expected_cities = list(range(2, 21))
    
    if sorted(all_cities_visited) != expected_cities:
        return "FAIL: Not all cities are visited exactly once by both robots together."

    # Calculate actual travel costs and verify
    def calculate_tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            cost += euclidean_distance(*coordinates[city1], *coordinates[city2])
        return cost

    calculated_cost_0 = calculate_tour_cost(robot_0_tour)
    if not math.isclose(calculated_cost_0, robot_0_cost, rel_tol=1e-5):
        return f"FAIL: Calculated cost for Robot 0 does not match. Expected: {robot_0_cost}, Got: {calculated_cost_0}"

    calculated_cost_1 = calculate_tour_cost(robot_1_tour) if robot_1_tour else 0
    if not math.isclose(calculated_cost_1, robot_1_cost, rel_tol=1e-5):
        return f"FAIL: Calculated cost for Robot 1 does not match. Expected: {robot_1_cost}, Got: {calculated_cost_1}"

    if not math.isclose(calculated_cost_0 + calculated_cost_1, overall_cost, rel_tol=1e-5):
        return f"FAIL: Overall cost does not match. Expected: {overall_cost}, Got: {calculated_cost_0 + calculated_cost_1}"

    return "CORRECT"
    
# Given solution details
robot_0_tour = [0, 16, 6, 20, 5, 14, 17, 9, 13, 2, 7, 8, 18, 19, 3, 12, 15, 11, 4, 10, 1, 0]
robot_0_cost = 188.5266456486993
robot_1_tour = []
robot_1_cost = 0
overall_cost = 188.5266456486993

# City coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Verify the solution
result = verify_solution(
    [robot_0_tour, robot_1_tour],
    [robot_0_cost, robot_1_cost],
    city_coordinates
)

print(result)  # Output the result based on verification