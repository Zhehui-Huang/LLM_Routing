def test_solution():
    # Provided solution
    robot_0_tour = [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0]
    robot_1_tour = [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]
    robot_0_cost = 212.21732723337922
    robot_1_cost = 184.31166515759514
    max_travel_cost = 212.21732723337922

    all_cities = set(range(1, 21))  # City indices excluding the depot (0)

    # Requirement 1: Each city, except the depot, visited once across all robots
    visited_cities = set(robot_0_tour + robot_1_tour) - {0}
    assert visited_cities == all_cities, "Not all cities are visited or some are visited more than once."

    # Requirement 2: Both tours start and end at the depot
    assert robot_0_tour[0] == robot_0_tour[-1] == 0, "Robot 0's tour does not start and end at the depot."
    assert robot_1_tour[0] == robot_1_tour[-1] == 0, "Robot 1's tour does not start and end at the depot."

    # Requirement 5: Output tours which are lists that start and end at the depot city
    assert robot_0_tour[0] == robot_0_tour[-1] == 0, "Robot 0's output does not meet format requirements."
    assert robot_1_tour[0] == robot_1_tour[-1] == 0, "Robot 1's output does not meet format requirements."

    # Requirement 6: Correct reporting of travel cost and maximum travel cost
    max_reported_cost = max(robot_0_cost, robot_1_cost)
    assert max_reported_cost == max_travel_cost, "Max travel cost does not match the higher of individual costs."

    print("CORRECT")

# Running the test function
test_solution()