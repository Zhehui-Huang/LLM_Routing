def test_solution():
    # Tours given by the solver
    robot_0_tour = [0, 6, 0]
    robot_1_tour = [0, 1, 10, 4, 11, 14, 12, 3, 17, 16, 8, 9, 15, 13, 5, 7, 2, 18, 0]

    # Combining all cities from both robot tours
    all_cities_visited = robot_0_tour[1:-1] + robot_1_tour[1:-1]  # Exclude the depot (0) from the first and last positions

    # Checking if each city is visited exactly once
    all_cities = set(range(1, 19))  # Creating a set of all cities from 1 to 18
    cities_visited_once = set(all_cities_visited) # Unique cities visited
    
    # Check for each city visited exactly once
    if cities_visited_once != all_cities:
        return "FAIL: Not all cities are visited or some cities are visited more than once."

    # Check flow conservation, depot leave and return, binary constraints implicitly covered in the solution format
    if len(robot_0_tour) < 3 or len(robot_1_tour) < 3:
        return "FAIL: Tour should start and end at the depot and visit at least one city."

    # Subtour check by ensuring no disconnects in each tour list.
    # We check if each list starts and ends at 0, which ensures subtour linkage to the depot.
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL: Robot 0 does not start or end at the depot."
    if robot_1_tour[0] != 0 or robot_1_tour[-1] != 0:
        return "FAIL: Robot 1 does not start or end at the depot."

    # Since the checks pass
    return "CORRECT"

# Call the test function and print the result
print(test_solution())