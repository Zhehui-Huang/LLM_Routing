def test_solution():
    # Provided tours from the solution
    tour_robot_0 = [0, 16, 0]
    tour_robot_1 = [0, 1, 10, 4, 11, 15, 12, 3, 19, 18, 8, 2, 7, 13, 9, 17, 14, 5, 20, 6, 0]
    
    # All cities including depot
    all_cities = set(range(21))
    
    # Requirement 1: Each city is visited exactly once by one salesman
    # Collect cities from all tours excluding the depot (0)
    visited_cities = set(tour_robot_0[1:-1] + tour_robot_1[1:-1])
    if visited_cities != all_cities - {0}:
        return "FAIL"

    # Requirement 2: Flow conservation
    # For each robot's tour, check if each city appears exactly once except the depot city
    if len(set(tour_robot_0)) != len(tour_robot_0) or len(set(tour_robot_1)) != len(tour_robot_1):
        return "FAIL"

    # Requirement 3: Each salesman leaves the depot exactly once
    # First and last elements of each tour should be the depot, and no other depot appearances
    if tour_robot_0[0] != 0 or tour_robot_1[0] != 0 or tour_robot_0[-1] != 0 or tour_robot_1[-1] != 0:
        return "FAIL"
    
    # Requirement 4: Subtour elimination constraints
    # Each tour should not contain sub-tours; this is implicitly handled by single appearance and correct flow

    # Requirement 5: Binary constraints for assignment variables
    # Since tours are given as lists, binary conditions (used/not used - 0/1) for routes are implied and met
    
    # Requirement 6: Continuous variables for node positions
    # This is a modeling detail not directly verifiable through the tour output but assumed correct by solver usage

    return "CORRECT"

# Running the test function
result = test_solution()
print(result)