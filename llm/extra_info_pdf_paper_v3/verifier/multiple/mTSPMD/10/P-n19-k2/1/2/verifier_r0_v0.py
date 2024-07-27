import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    tour_robot_0 = [0, 8, 2, 7, 13, 10, 11, 4, 16, 17, 3, 15, 9, 5, 18, 14, 12, 6, 0]
    tour_robot_1 = [1, 18, 14, 15, 13, 4, 7, 5, 2, 8, 16, 17, 3, 11, 6, 9, 10, 12, 1]
    
    # Calculate tour costs
    cost_robot_0, cost_robot_1 = 0, 0
    for i in range(1, len(tour_robot_0)):
        cost_robot_0 += calculate_distance(cities[tour_robot_0[i-1]], cities[tour_robot_0[i]])
    for i in range(1, len(tour_robot_1)):
        cost_robot_1 += calculate_distance(cities[tour_robot_1[i-1]], cities[tour_robot_1[i]])
        
    total_cost = cost_robot_0 + cost_robot_1

    # Check uniqueness of city visits excluding the depots
    all_cities_visited = set(tour_robot_0[1:-1] + tour_robot_1[1:-1])
    if len(all_cities_visited) != 18 or set(all_cities_visited) != set(range(2, 19)):
        print("FAIL: Not all cities are visited or there are duplicate visits.")
        return "FAIL"

    # Check if each robot returns to the correct depot
    if tour_robot_0[0] != tour_robot_0[-1] or tour_robot_0[0] != 0:
        print("FAIL: Robot 0 does not start and end at the correct depot.")
        return "FAIL"
    if tour_robot_1[0] != tour_robot_1[-1] or tour_robot_1[0] != 1:
        print("FAIL: Robot 1 does not start and end at the correct depot.")
        return "FAIL"
    
    # Validate against reported costs - tolerating small floating point deviations
    reported_cost_0, reported_cost_1 = 281.61536536015274, 244.79356782158115
    if not (abs(cost_robot_0 - reported_cost_0) < 0.01 and abs(cost_robot_1 - reported_cost_1) < 0.01 and abs(total_cost - 526.4089331817339) < 0.01):
        print("FAIL: Computed costs do not match reported costs.")
        return "FAIL"
    
    print("CORRECT")
    return "CORRECT"

test_solution()