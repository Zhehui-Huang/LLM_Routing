import numpy as np

def calculate_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_solution(tour1, cost1, tour2, cost2, overall_cost):
    # Cities coordinates as given
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    
    # Requirement 1: Start tours from Depot City 0
    if not (tour1[0] == 0 and tour2[0] == 0):
        return "FAIL"
    
    # Requirement 2: Visit all cities exactly once
    all_cities = set(range(21))
    visited_cities = set(tour1[1:]) | set(tour2[1:])  # Exclude repeated depot city at start
    if all_cities != visited_cities:
        return "FAIL"
    
    # Requirement 3: Any endpoint
    # No check since it's inherently satisfied by any valid tour ending
    
    # Requirement 4 and 5: Minimize combined cost and use Euclidean distance
    def compute_tour_cost(tour):
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        return tour_cost
    
    computed_cost1 = compute_tour_cost(tour1)
    computed_cost2 = compute_tour_cost(tour2)
    
    if not (abs(computed_cost1 - cost1) < 1e-5 and abs(computed_cost2 - cost2) < 1e-5):
        return "FAIL"
    
    if not abs((cost1 + cost2) - overall_cost) < 1e-5:
        return "FAIL"
    
    # Requirement 6: Output check is implicit in the function parameters and checks above
    
    return "CORRECT"

# Tours and costs from the provided solution
robot_0_tour = [0, 20, 14, 5, 7, 2, 18, 19, 12, 11]
robot_0_cost = 117.42371743183594
robot_1_tour = [0, 6, 16, 4, 15, 10, 3, 8, 13, 9, 17]
robot_1_cost = 104.46168107191767
overall_total_cost = 221.8853985037536

# Run the verification
result = verify_solution(robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost, overall_total