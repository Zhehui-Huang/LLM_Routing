import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(robot_tours, cities, robots=2):
    visited_cities = set()
    total_calculated_cost = 0
    
    if len(robot_tours) != robots:
        return "FAIL"
    
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Requirement 3
        prev_city = tour[0]
        for city_index in tour[1:]:
            if city_index != 0:  # Exclude the depot for the visited cities check
                visited_cities.add(city_index)
            # Calculate the travel cost
            total_calculated_cost += calculate_distance(cities[prev_city], cities[city_index])
            prev_city = city_index
    
    # Requirement 4
    if visited_cities != set(range(1, 21)):
        return "FAIL"
    
    # Compare the calculated total cost with provided cost as per Requirement 6
    # Let's assume provided_cost is received from some other part of the system, here we manually set it
    provided_cost = 327.04034846960514
    if abs(provided_cost - total_calculated_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates configuration as per the problem description
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours as per the provided solution
robot_tours = [
    [0, 1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 0],
    [0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0]
]

# Test the solution
result = verify_solution(robot_tours, cities_coordinates)
print(result)