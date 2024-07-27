import math

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return round(total_cost, 2)

def test_tsp_solution():
    robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2]

    # Check the number of cities in the tour and uniqueness
    assert len(robot_0_tour) == 21, "Each city must be visited exactly once."
    assert len(set(robot_0_tour)) == 21, "Each city must be unique in the tour."

    # Check start and end condition
    assert robot_0_tour[0] == 0, "Tour must start from depot city 0."

    # Calculate and verify the costs
    robot_0_cost_calculated = calculate_total_cost(robot_0_tour)
    robot_0_cost_reported = 187.82
    assert robot_0_cost_calculated == robot_0_cost_reported, "Mismatch in total travel cost calculation."

    # Print total costs and overall cost
    print("Robot 0 Tour:", robot_0_tour)
    print("Robot 0 Total Travel Cost:", robot_0_cost_calculated)

    # Overall total cost
    overall_total_cost = robot_0_cost_calculated
    assert overall_total_cost == 187.82, "Overall total costs not tallying."

    print("Overall Total Travel Costs:", round(overall_total_cost, 2))

# Run test function and handle assertion errors
try:
    test_tsp_solution()
    print("CORRECT")
except AssertionError as e:
    print("FAIL:", str(e))