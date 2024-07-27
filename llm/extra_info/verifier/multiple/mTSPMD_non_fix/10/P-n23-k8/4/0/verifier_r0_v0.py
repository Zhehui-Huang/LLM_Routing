import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution():
    # Define city coordinates
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    
    # Robot tours provided in the solution
    robot_tours = [
        [0, 21],
        [1, 16, 10],
        [2, 13],
        [3, 8, 18, 19, 12],
        [4, 11, 15],
        [5, 22, 7, 9, 17, 14],
        [6, 20]
    ]
    
    # Verify Requirement 1: Visit all cities exactly once
    visited_cities = [city for tour in robot_tours for city in tour]
    if len(set(visited_cities)) != len(cities) or len(visited_cities) != len(cities):
        return "FAIL"
    
    # Verify Requirement 2: Start from depot city 0 for each robot
    if not all(tour[0] == 0 for tour in robot_tours):
        return "FAIL"
    
    # Verify Requirement 3: Calculate actual total cost and compare with expected
    expected_total_cost = 131.23910211225785
    actual_total_cost = 0

    for tour in robot_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_cost += tour_cost

    if not math.isclose(actual_total_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Run the verification function
output = verify_solution()
print(output)