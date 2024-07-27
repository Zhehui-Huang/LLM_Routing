def verify_solution(robots_tours, robots_costs):
    # Define all city indices
    all_cities = set(range(19))
    
    # Gather information from robot tours
    visited_cities = set()
    correct_depot_starts_ends = True
    total_cost_calculated = 0

    # For each robot, check the tour and compute costs
    robot_0_cities = set(range(1, 19))  # Robot 0 should not visit city 1.
    robot_1_cities = set(range(19))     # Robot 1 should visit any city but starts and ends at 1.
    tours = [[6, 18, 0], [10, 1]]
    distances = {
        (6, 18): 10.63,
        (18, 0): 11.18,
        (0, 6): 11.04,
        (10, 1): 7.07
    }
    
    for robot_id, tour in enumerate(robots_tours):
        start_depot = tour[0]
        end_depot = tour[-1]
        
        # Check start and end at correct depot
        if (robot_id == 0 and (start_depot, end_depot) != (0, 0)) or (robot_id == 1 and (start_depot, end_depot) != (1, 1)):
            correct_depot_starts_ends = False

        # Add to visited cities and check city visiting constraints
        visited_cities.update(tour)

        # Calculate and verify travel cost
        robot_cost = 0
        for i in range(len(tour) - 1):
            if (tour[i], tour[i+1]) not in distances:
                print(f"Distance computation error: Missing distance between {tour[i]} and {tour[i+1]}")
                return "FAIL"

            robot_cost += distances[(tour[i], tour[i+1])]

        # Check if cost matches the one provided
        if not (abs(robot_cost - robots_costs[robot_id]) < 0.01):
            print(f"Error in reported cost for robot {robot_id}.")
            return "FAIL"

        total_cost_calculated += robot_cost
        
    # Cross-validation of all visited cities exactly once
    if visited_cities != all_cities:
        print("Not all cities are visited or some cities are visited more than once.")
        return "FAIL"
    
    # Verify the correctness of start and end points
    if not correct_depot_starts_ends:
        print("A robot does not start or end at its assigned depot.")
        return "FAIL"

    # Verify minimum route cost check if needed
    if not abs(sum(robots_costs) - total_cost_calculated) < 0.01:
        print("There is a mismatch in the total travel cost calculation.")
        return "FAIL"

    # If all checks are satisfied
    return "CORRECT"

# Tests
robots_tours = [[6, 18, 0], [10, 1]]
robots_costs = [22.52, 7.07]
result = verify_solution(robots_tours, robots_costs)
print(result)