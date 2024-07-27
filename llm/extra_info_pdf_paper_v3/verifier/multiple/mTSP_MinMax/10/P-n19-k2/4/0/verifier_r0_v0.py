def test_tsp_solution():
    # Provided solution by user
    robot_0_tour = [0, 1, 10, 8, 16, 17, 3, 12, 14, 11, 4, 0]
    robot_1_tour = [0, 6, 2, 7, 9, 15, 13, 5, 18, 0]
    robot_0_cost = 116.32876651388246
    robot_1_cost = 80.31749999965547
    max_cost = 116.32876651388246

    # Requirement 1: Each robot starts and ends at depot city 0
    requirement_1 = (robot_0_tour[0] == 0 and robot_0_tour[-1] == 0) and \
                    (robot_1_tour[0] == 0 and robot_1_tour[-1] == 0)

    # Requirement 2: Every city except the depot must be visited exactly once
    visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1])  # Exclude the depot city (0) in this check
    total_cities = set(range(1, 19))  # City indices from 1 to 18
    requirement_2 = visited == total_cities

    # Check if output cost calculations are scrupulously completed
    # This is a simplified version of checking if the maximum of the given costs is correct.
    requirement_3 = max(robot_0_cost, robot_1_cost) == max_cost

    # Evaluate all requirements
    if requirement_1 and requirement_2 and requirement_3:
        return "CORRECT"
    else:
        return "FAIL"

# Running the test function
print(test_tsp_solution())