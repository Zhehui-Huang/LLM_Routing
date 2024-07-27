import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    # City coordinates
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69)
    }

    # Given solution
    robot_0_tour = [0, 13, 15, 8, 5, 7, 10, 12, 3, 11, 14, 9, 6, 2, 4, 1, 0]
    expected_cost = 324.19974012142717
    
    # Check if all cities are visited exactly once (excluding the depot, which should appear twice)
    for city in range(1, 16):
        if city not in robot_0_tour:
            print("FAIL")
            return
    if robot_0_tour.count(0) != 2:
        print("FAIL")
        return

    # Calculate the travel cost
    calculated_cost = 0
    for i in range(len(robot_0_tour)-1):
        x1, y1 = cities[robot_0_tour[i]]
        x2, y2 = cities[robot_0_tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Check if the calculated cost is correctly given
    if not (abs(calculated_cost - expected_cost) < 0.00001):
        print("FAIL")
        return
    
    print("CORRECT")

test_solution()