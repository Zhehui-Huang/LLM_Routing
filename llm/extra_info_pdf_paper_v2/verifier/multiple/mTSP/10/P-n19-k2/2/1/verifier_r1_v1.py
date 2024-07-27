import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, city_coordinates, reported_total_cost):
    visited_cities = set()
    all_cities_set = set(range(1, len(city_coordinates)))  # City indices excluding the depot
    
    total_travel_cost = 0.0
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Requirement 2 check
        
        previous_city_index = tour[0]
        for city_index in tour[1:]:
            if city_index != 0:  # The depot city can be revisited only as start or end, not in between
                visited_cities.add(city_index)
            edge_cost = calculate_distance(city_coordinates[previous_city_index], city_coordinates[city_index])
            total_travel_cost += edge_cost
            previous_city_index = city_index
    
    if visited_cities != all_cities_set:
        return "FAIL"  # Requirement 1 check
        
    if not math.isclose(total_travel_cost, reported_total_cost, abs_tol=1e-2):
        return "FAIL"  # Requirement 3 check, tolerates small floating-point deviations
    
    return "CORRECT"

# Coordinates of each city, including the depot
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution details
robot_tours = [
    [0, 11, 4, 1, 18, 17, 16, 3, 12, 14, 6, 15, 13, 2, 7, 5, 0],
    [0, 10, 8, 9, 0]
]
reported_total_cost = 329.72  # Best overall total cost extracted from the solution provided

# Verify the solution
solution_status = verify_solution(robot_tours, city_coordinates, reported_total_cost)
print(solution_status)