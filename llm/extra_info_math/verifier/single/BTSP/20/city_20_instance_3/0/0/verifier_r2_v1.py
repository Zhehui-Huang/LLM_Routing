def test_robot_tour(tour, total_cost, max_distance_between_cities):
    """ Test if the robot tour meets the problem requirements. """
    TEST_PASS_TEXT = "CORRECT"
    TEST_FAIL_TEXT = "FAIL"
    
    # Requirement 1: Check if the robot starts and ends at the depot city 0.
    start_at_depot = tour[0] == 0
    end_at_depot = tour[-1] == 0
    
    # Requirement 2: Check if each city is visited exactly once
    cities_visited = set(tour[1:-1]) # Including cities between start and the last 0 (end)
    
    # Expect all unique cities from 1 to 19 (since 0 is the depot)
    expected_cities = set(range(1, 20))
    
    visit_once = cities_visited == expected_cities and tour.count(0) == 2
    
    if start_at_depot and end_at_depot and visit_once:
        return TEST_PASS_TEXT
    else:
        return TEST_FAIL_TEXT

# Tour and values from solver output
tour = [0, 3, 4, 5, 19, 7, 15, 13, 14, 12, 11, 1, 10, 18, 2, 8, 17, 9, 16, 0, 6, 0]
total_cost = 1066.6985439820317
max_distance_between_cities = 107.42439201596628

# Call the test function
result = test_robot_tour(tour, total_cost, max_distance_between_cities)
print(result)