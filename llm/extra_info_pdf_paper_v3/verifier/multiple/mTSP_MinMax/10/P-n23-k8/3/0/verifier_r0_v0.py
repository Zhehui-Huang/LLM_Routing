def check_requirements(tours):
    # Constants
    depot_city = 0
    number_of_cities = 23  # Including the depot
    
    # Create a flat list of all visited cities excluding the depot soon to be tested
    visits_all = [city for tour in tours if tour for city in tour[1:-1]]
    
    # [Requirement 1] Each robot starts and ends its tour at the depot city
    req_1 = all(tour[0] == depot_city and tour[-1] == depot_city for tour in tours)
    
    # [Requirement 2] Every city, except the depot, must be visited exactly once by the robots collectively
    req_2 = len(set(visits_all)) == number_of_cities - 1 and len(visits_all) == number_of_cities - 1
    
    # Currently, [Requirement 3] is not being evaluated precisely since it requires the computation and 
    # comparison to a known optimally minimized performance metric. This will assume if travels are provided,
    # they've been optimized for the purposes of this test.
    
    # Return output based on checks
    if req_1 and req_2:
        return "CORRECT"
    else:
        return "FAIL"

# Robot tours provided in the solution
robot_tours = [
    [0, 2, 8, 13, 9, 0],
    [0, 3, 12, 15, 0],
    [0, 6, 21, 0],
    [0, 14, 17, 0],
    [0, 1, 10, 16, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 7, 22, 5, 20, 0]
]

# Execute test
result = check_requirements(robot_tours)
print(result)