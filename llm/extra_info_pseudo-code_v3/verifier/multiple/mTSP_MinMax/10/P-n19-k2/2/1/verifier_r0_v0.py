import math

# City coordinates as given in the problem description
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Provided solution
solution = {
    "robot_0": [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0],
    "robot_1": [0, 6, 18, 5, 7, 2, 9, 15, 13, 0],
    "cost_0": 143.98241284438606,
    "cost_1": 97.30815163794452,
    "max_cost": 143.98241284438606
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
    # Test the cities are visited exactly once except the depot
    all_cities_visited = set(solution["robot_0"] + solution["robot_1"])
    if all_cities_visited != set(range(19)):
        return "FAIL"
    
    # Test each robot tour starts and ends at the city 0
    if solution["robot_0"][0] != 0 or solution["robot_0"][-1] != 0:
        return "FAIL"
    if solution["robot_1"][0] != 0 or solution["robot_1"][-1] != 0:
        return "FAIL"

    # Calculate and verify the costs provided
    def calculate_total_cost(tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        return total_cost
    
    calculated_cost_0 = calculate_total_cost(solution["robot_0"])
    calculated_cost_1 = calculate_total_cost(solution["robot_1"])
    calculated_max_cost = max(calculated_cost_0, calculated_cost_1)

    if not math.isclose(calculated_cost_0, solution["cost_0"], rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_cost_1, solution["cost_1"], rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_cost, solution["max_cost"], rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Running the test
test_output = test_solution()
print(test_output)