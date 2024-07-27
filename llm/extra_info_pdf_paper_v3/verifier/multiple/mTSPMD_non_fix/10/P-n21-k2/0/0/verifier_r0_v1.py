import numpy as np

def calculate_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_solution(tour1, cost1, tour2, cost2, overall_cost):
    # Define the coordinates for the cities
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    
    # Check the tours start at the depot and cover all cities exactly once
    if tour1[0] != 0 or tour2[0] != 0:
        return "FAIL"

    all_visited = set(tour1 + tour2)
    if all_visited != set(range(21)):
        return "FAIL"

    # Calculate the correct travel costs using the Euclidean distance
    def compute_tour_cost(tour):
        cost = 0.0
        for i in range(1, len(tour)):
            cost += calculate_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
        return cost
    
    computed_cost1 = compute_tour_cost(tour1)
    computed_cost2 = compute_tour_cost(tour2)

    # Check if the costs are accurate and the total cost sums up correctly
    if not (abs(computed_cost1 - cost1) < 1e-5 and abs(computed_cost2 - cost2) < 1e-5):
        return "FAIL"
    if not abs((cost1 + cost2) - overall_cost) < 1e-5:
        return "FAIL"

    return "CORRECT"

# Provided tours and costs
robot_0_tour = [0, 20, 14, 5, 7, 2, 18, 19, 12, 11]
robot_0_cost = 117.42371743183594
robot_1_tour = [0, 6, 16, 4, 15, 10, 3, 8, 13, 9, 17]
robot_1_cost = 104.46168107191767
overall_total_cost = 221.8853985037536

# Execute the verification
result = verify_solution(robot_0_tour, robot_0_cost, robot_1_tour, robot_1_cost, overall_total_cost)
print(result)