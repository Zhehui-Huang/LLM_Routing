import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, city_coordinates):
    visited_cities = set()
    total_calculated_cost = 0
    
    for tour in robot_tours:
        # Requirement 1: Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate and verify travel costs
        tour_cost = 0
        for i in range(len(tour) - 1):
            distance = calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            tour_cost += distance

        # Accumulate total travel cost for all robots
        total_calculated_cost += tour_cost
        
        # Collect all visited cities excluding the depot
        visited_cities.update(tour[1:-1])

    # Requirement 2: All cities except depot are visited exactly once
    if visited_cities != set(range(1, len(city_coordinates))):
        return "FAIL"
    
    # Check the accumulated cost against expected total cost
    if total_calculated_cost - 302.8390611127802 > 1e-9:  # Comparing floating-point numbers with a tolerance
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# City coordinates based on the given tours assignment
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Given tours and their costs
robot_0_tour = [0, 6, 18, 2, 1, 10, 12, 14, 4, 8, 16, 0]
robot_1_tour = [0, 7, 5, 13, 15, 9, 3, 17, 11, 0]

# Verify the solution using the test function
result = verify_solution([robot_0_tour, robot_1_tour], cities)
print(result)