import numpy as np
from scipy.spatial.distance import euclidean

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 30), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }
    
    # Robot tours
    robot_0_tour = [0, 6, 7, 5, 14, 13, 8, 18, 3, 1, 11, 0]
    robot_1_tour = [0, 16, 2, 10, 12, 15, 4, 20, 17, 9, 19, 0]
    
    # Reported costs
    reported_cost_0 = 152.93528566420733
    reported_cost_1 = 184.16986619389235
    reported_total_cost = 337.1051518580997
    
    def calculate_tour_cost(tour):
        cost = 0.0
        for i in range(len(tour) - 1):
            cost += euclidean(cities[tour[i]], cities[tour[i+1]])
        return cost

    # Calculate tour costs
    calc_cost_0 = calculate_tour_cost(robot_0_tour)
    calc_cost_1 = calculate_tour_cost(robot_1_tour)
    calc_total_cost = calc_cost_0 + calc_cost_1
    
    # Check cost calculations within a small margin of error
    if not (np.isclose(calc_cost_0, reported_cost_0, atol=1e-5) and
            np.isclose(calc_cost_1, reported_cost_1, atol=1e-5) and
            np.isclose(calc_total_cost, reported_total_cost, atol=1e-5)):
        return "FAIL"
    
    # Check if all cities are visited exactly once excluding depot
    visited = set(robot_0_tour + robot_1_tour)
    if visited != set(range(21)) or robot_0_tour.count(0) != 2 or robot_1_tour.count(0) != 2:
        return "FAIL"
    
    return "CORRECT"

# Invoke the testing function
result = test_solution()
print(result)