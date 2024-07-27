import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_cost(tour, coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def test_solution():
    # Provided solution tours and costs
    solution_robot_0_tour = [0, 1, 10, 8, 16, 17, 3, 12, 14, 11, 4, 0]
    solution_robot_0_cost = 116.32876651388246
    solution_robot_1_tour = [0, 6, 2, 7, 9, 15, 13, 5, 18, 0]
    solution_robot_1_cost = 80.31749999965547
    combined_cost = 196.6462665135379
    
    # City coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Check requirements
    all_cities_visited = set(solution_robot_0_tour + solution_robot_1_tour) == set(range(19))
    tours_start_end_depot = solution_robot_0_tour[0] == solution_robot_0_tour[-1] == 0\
                            and solution_robot_1_tour[0] == solution_robot_1_tour[-1] == 0
    calculated_robot_0_cost = calculate_total_cost(solution_robot_0_tour, coordinates)
    calculated_robot_1_cost = calculate_total_cost(solution_robot_1_tour, coordinates)
    
    # Cost within a tolerance due to floating-point arithmetic
    cost_within_tolerance = np.isclose(calculated_robot_0_cost, solution_robot_0_cost, atol=0.001)\
                            and np.isclose(calculated_robot_1_cost, solution_robot_1_cost, atol=0.001)\
                            and np.isclose(calculated_robot_0_cost + calculated_robot_1_cost, combined_cost, atol=0.001)
    
    if all([all_cities_visited, tours_start_end_depot, cost_within_tolerance]):
        print("CORRECT")
    else:
        print("FAIL")

test_solution()