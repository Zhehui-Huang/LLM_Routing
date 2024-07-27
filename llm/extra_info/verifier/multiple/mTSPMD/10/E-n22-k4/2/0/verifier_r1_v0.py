import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
    cities = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
        6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
        18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
    }
    
    robot0_tour = [0, 14, 16, 13, 11, 8, 6, 10, 9, 7, 5, 2, 1, 3, 4, 12, 15, 18, 20, 21, 19, 17, 0]
    robot0_cost = 454.389609282707
    
    # Check if robot starts and ends at the correct depot
    if robot0_tour[0] != robot0_tour[-1] != 0:
        return "FAIL"
    
    # Check if all robots visit all cities exactly once
    unique_cities_visited = set(robot0_tour[1:-1])  # exclude start and end depot city
    if len(unique_cities_visited) != 21:  # check if 21 unique cities were visited
        return "FAIL"

    # Calculate and verify the total travel cost for robot 0
    calculated_cost = 0
    for i in range(len(robot0_tour) - 1):
        start_city = robot0_tour[i]
        end_city = robot0_tour[i + 1]
        calculated_cost += euclidean_distance(cities[start_city], cities[end_city])
    
    if not math.isclose(calculated_cost, robot0_cost, rel_tol=1e-6):
        return "FAIL"
    
    # Overall Total Travel Cost
    expected_total_travel_cost = 454.389609282707
    if not math.isclose(calculated_cost, expected_total_travel_exports_cost, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_solution())