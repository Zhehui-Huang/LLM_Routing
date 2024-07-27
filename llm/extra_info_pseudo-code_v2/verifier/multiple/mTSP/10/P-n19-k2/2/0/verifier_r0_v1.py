import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # Provided robot tours
    robot_0_tour = [0, 1, 10, 4, 14, 12, 16, 15, 5, 18, 0]
    robot_1_tour = [0, 6, 2, 7, 13, 9, 8, 17, 3, 11, 0]
    
    # Provided costs
    provided_robot_0_cost = 130.12
    provided_robot_1_cost = 148.54
    provided_total_cost = 278.65

    # City coordinates
    city_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        16: (62, 63), 15: (61, 33), 17: (63, 69), 18: (45, 35)
    }

    # Calculate costs for provided tours
    def calculate_tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            x1, y1 = city_coords[city1]
            x2, y2 = city_coords[city2]
            cost += calculate_euclidean_distance(x1, y1, x2, y2)
        return cost

    calculated_cost_robot_0 = calculate_tour_cost(robot_0_tour)
    calculated_cost_robot_1 = calculate_tour_cost(robot_1_tour)
    calculated_total_cost = calculated_cost_robot_0 + calculated_cost_robot_1

    # Check if calculated and provided costs are almost equal (tolerance due to floating point precision)
    if not math.isclose(calculated_cost_robot_0, provided_robot_0_cost, rel_tol=1e-2) or \
       not math.isclose(calculated_cost_robot_1, provided_robot_1_cost, rel_tol=1e-2) or \
       not math.isclose(calculated_total_cost, provided_total_overall_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Ensure all cities are visited exactly once (except depot)
    all_visited_cities = set(robot_0_tour + robot_1_tour)
    if len(all_visited_cities) != 19 or 0 not in all_visited_cities:
        return "FAIL"

    # Check if each city, except the depot (0), appears exactly once
    city_visit_count = {key: 0 for key in range(1, 19)}
    for city in robot_0_tour[1:-1] + robot_1_tour[1:-1]:
        city_visit_count[city] += 1

    if any(count != 1 for count in city_visit_count.values()):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution()
print(result)