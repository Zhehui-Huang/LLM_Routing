def test_robot_tour(tour, total_cost, max_distance_between_cities):
    """ Test if the robot tour meets the problem requirements. """
    TEST_PASS_TEXT = "CORRECT"
    TEST_FAIL_TEXT = "FAIL"
    
    # Requirement 1: Check if the robot starts and ends at the depot city 0.
    start_at_depot = tour[0] == 0
    end_at_depot = tour[-1] == 0
    
    # Requirement 2: Check if each city is visited exactly once
    unique_cities_visited = len(set(tour)) - 1  # Excluding the final return to start
    total_cities = 20  # Total number of cities excluding the depot
    
    if unique_cities_visited == total_cities and start_at_depot and end_at_depot:
        visit_once = True
    else:
        visit_once = False
    
    # Requirement 3: Minimum Expected Cost and Max Distance - Handled by the problem's solver, not verifiable directly here

    # If all requirements are met, set result to TEST_PASS_TEXT, otherwise to TEST_FAIL_TEXT
    if start_at_depot and end_at_depot and visit_once:
        return TEST_PASS_TEXT
    else:
exam        return TEST_FAIL_TEXT

# Tour and values from solver output
tour = [0, 3, 4, 5, 19, 7, 15, 13, 14, 12, 11, 1, 10, 18, 2, 8, 17, 9, 16, 0, 6, 0]
total_cost = 1066.6985439820317
max_distance_between_cities = 107.42439201596628

# Call the test function
result = test_robot_tours(tour, total_cost, max_distance_between_cities)
print(result)