import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def compute_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        cost += euclidean_distance(x1, y1, x2, y2)
    return cost

def test_solution():
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
        16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    # Provided solution details
    robot0_tour = [0, 9, 17, 12, 13, 18, 1, 14, 4, 8]
    robot0_cost_provided = 208.47879030855924
    robot1_tour = [0, 5, 11, 10, 16, 3, 15, 7, 2, 6]
    robot1_cost_provided = 170.83726349979852
    overall_cost_provided = 379.31605380835776
    
    # Compute costs for comparison
    calculated_robot0_cost = compute_cost(robot0_tour + [robot0_tour[-1]], coordinates)
    calculated_robot1_cost = compute_cost(robot1_tour + [robot1_tour[-1]], coordinates)
    calculated_overall_cost = calculated_robot0_cost + calculated_robot1_cost
    
    # Check if all cities are covered exactly once
    city_visits = robot0_tour + robot1_tour
    if len(set(city_visits)) != 19 or set(city_visits) != set(range(19)):
        return "FAIL: Cities visited check"

    # Check cost computations
    if not math.isclose(robot0_cost_provided, calculated_robot0_cost, rel_tol=1e-6) or not math.isclose(robot1_cost_provided, calculated_robot1_cost, rel_tol=1e-6):
        return "FAIL: Cost calculation check"

    if not math.isclose(overall_cost_provided, calculated_overall_cost, rel_tol=1e-6):
        return "FAIL: Overall cost check"

    return "CORRECT"

# Call to test function
print(test_solution())