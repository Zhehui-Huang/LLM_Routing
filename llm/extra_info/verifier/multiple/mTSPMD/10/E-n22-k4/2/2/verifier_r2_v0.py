import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution():
    # City coordinates
    cities = [
        (145, 215), (151, 264), (159, 261), (130, 254),
        (128, 252), (163, 247), (146, 246), (161, 242),
        (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208),
        (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    
    robot_tours = [
        [0, 14, 16, 17, 20, 18, 0],
        [1, 6, 8, 10, 12, 21, 1],
        [2, 5, 7, 9, 15, 2],
        [3, 4, 11, 13, 19, 3]
    ]
    
    provided_costs = [79.19824046755065, 174.7468942349509, 107.52311797510075, 130.8655053432526]
    
    # 1. Check if all cities are covered exactly once and each tour starts and ends at its depot
    all_visited_cities = set()
    for tour in robot_tours:
        if tour[0] != tour[-1]:  # start and end at depot
            return "FAIL"
        all_visited_cities.update(tour)

    if len(all_visited_cities) != 22:  # Some city might be missing or duplicated
        return "FAIL"

    # 2. Calculate actual costs
    total_calculated_cost = 0
    for robot_id, tour in enumerate(robot_tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += compute_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if not math.isclose(tour_cost, provided_costs[robot_id], rel_tol=1e-9):
            return "FAIL"
        total_calculated_cost += tour_cost
    
    # 3. Check if total cost is correct
    provided_total_cost = 492.33375802085493
    if not math.isclose(total_calculated_cost, provided_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the test
test_result = check_solution()
print(test_result)