import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(robot_0_tour, robot_1_tour, robot_0_cost, robot_1_cost, overall_cost):
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    # Check start and end at their depots
    if not (robot_0_tour[0] == robot_0_tour[-1] == 0):
        print("FAIL")
        return
    if not (robot_1_tour[0] == robot_1_tour[-1] == 1):
        print("FAIL")
        return
    
    # Check uniqueness of the visits excluding the depots
    combined_tours = robot_0_tour[1:-1] + robot_1_tour[1:-1]
    if len(set(combined_tours)) != len(cities) - 2:
        print("FAIL")
        return
    
    # Check correct travel cost calculation
    def calculate_total_cost(tour):
        total_distance = 0
        for i in range(1, len(tour)):
            total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        return total_distance

    calculated_cost_0 = calculate_total_cost(robot_0_tour)
    calculated_cost_1 = calculate_total_cost(robot_1_tour)

    if not (abs(calculated_cost_0 - robot_0_cost) < 1e-6 and
            abs(calculated_cost_1 - robot_1_cost) < 1e-6 and
            abs(calculated_cost_0 + calculated_cost_1 - overall_cost) < 1e-6):
        print("FAIL")
        return

    print("CORRECT")

# Example provided solution
robot_0_tour = [0, 0, 20, 17, 16, 14, 13, 9, 7, 6, 5, 2, 0]
robot_1_tour = [1, 1, 19, 18, 15, 12, 11, 10, 8, 4, 3, 1]
robot_0_cost = 0
robot_1_cost = 0
overall_cost = 0

check_solution(robot_0_tour, robot_1_tour, robot_0_cost, robot_1_cost, overall_cost)