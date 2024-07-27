def verify_solution(tours):
    # Total number of cities (including depot)
    total_cities = 22
    all_cities = set(range(total_cities))
    
    # Ensure each tour starts and ends at the depot
    each_start_end_with_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    if not each_start_end_with_depot:
        return "FAIL"
    
    # Collect all visited cities excluding depot in all tours
    visited_cities = [city for tour in tours for city in tour[1:-1]]  # Exclude the depot in this check
    
    # Check if each city is visited exactly once and only by one salesman
    if len(set(visited_cities)) != len(visited_cities):
        return "FAIL"
    if set(visited_cities) != (all_cities - {0}):
        return "FAIL"
    
    # Ensure all salesmen leave from and return to the depot precisely once per tour
    all_leave_return_depot = all(tour.count(0) == 2 for tour in tours)
    if not all_leave_return_depot:
        return "FAIL"
    
    # Here we assume that no subtours exist if all cities are visited exactly once and all tours start and end at the depot
    # Subtour checking without a solver involves more logic typically to ensure no loops within the tours excluding the depot.

    # Check for binary constraints being met
    if any(not (0 <= city < total_cities) for tour in tours for city in tour):
        return "FAIL"
    
    # If it passes all tests
    return "CORRECT"

# Provided Tours
robot_tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

# Validate the provided solution
result = verify_solution(robot_tours)
print(result)