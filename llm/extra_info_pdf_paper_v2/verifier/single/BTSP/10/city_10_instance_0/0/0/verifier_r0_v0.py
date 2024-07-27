import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # [Requirement 1] The robot starts and ends the route at the depot city (City 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once by the robot.
    if len(set(tour)) != len(cities) + 1 or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Check total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # [Requirement 5] The output should include the total travel cost of the tour.
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # [Requirement 6] The output should include the maximum distance between any two consecutive cities in the tour.
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Test solution with example data
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_cost = 365.33009275558874
max_distance = float('inf')  # This appears incorrect as max_distance should not be infinity

print(verify_solution(tour, total_cost, max_distance))