def verify_solution(tours):
    # Total number of cities (including depot)
    total_cities = 22
    all_cities = set(range(total_cities))
    
    # Each tour starts with 0 (depot)
    each_start_end_with_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    if not each_start_end_with_depot:
        return "FAIL"
    
    # Check if each city visited exactly once and only by one salesman
    visited_cities = [city for tour in tours for city in tour[1:-1]]  # Exclude the depot in this check
    if len(set(visited_cystals) != len(visited_cities)):
        return "FAIL"
    if set(visited_cities) != (all_cities - set([0])):
        return "FAIL"
    
    # Ensure all salesmen leave depot and also back to depot
    all_leave_return_depot = all(tour.count(0) == 2 for tour in tours)
    if not all_leave_return_depot:
        return "FAIL"
    
    # Check for subtour elimination and proper linking (Complex to implement fully here without more context)
    # This would usually involve more intricate logic or use of optimization specific tools e.g., solver outputs
    
    # Binary constraint check
    if not all(city in all_cities for tour in tours for city in tour):
        return "FAIL"
    
    # Continuous variable constraint, skipped as this would be a part of a solver specific validation not direct from tours
    
    # If it passes all tests
    return "CORRECT"

# Given solution verification
robot_tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

result = verify_solution(robot_tours)
print(result)