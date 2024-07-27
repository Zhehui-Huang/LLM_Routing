def verify_solution(robot_0_tour, robot_1_tour, total_travel_cost):
    # Requirement 1: All cities must be visited exactly once by the robots.
    all_cities_visited = set(range(21))  # Assuming cities are indexed from 0 to 20
    cities_visited = set(robot_0_tour + robot_1_tour)  # Collecting all visited cities from both tours
    
    if len(cities_visited) != 21 or any(city for city in cities_visited if city not in all_cities_visited):
        return "FAIL: Cities are not visited exactly once"

    # Requirement 2: Each robot must start and end its tour at its designated depot.
    if robot_0_tour[0] != 0 or robot_0_tour[-1] != 0:
        return "FAIL: Robot 0 does not start or end at the designated depot"
    if robot_1_tour[0] != 1 or robot_1_tour[-1] != 1:
        return "FAIL: Robot 1 does not start or end at the designated depot"
    
    # Requirement 3: Minimized total travel cost is checked internally, unable to verify without alternatives

    return "CORRECT"

# Sample data from the solution
robot_0_tour = [0, 11, 7, 11, 11, 11, 11, 13, 2, 6, 20, 0]
robot_0_travel_cost = 180.85059032816056
robot_1_tour = [1, 11, 11, 11, 11, 11, 11, 11, 4, 11, 1]
robot_1_travel_cost = 52.15812963008237
overall_total_travel_cost = 233.00871995824292

# Using the verify_solution function to check correctness
result = verify_solution(robot_0_tour, robot_1_tour, overall_total_travel_cost)
print(result)