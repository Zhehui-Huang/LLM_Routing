import numpy as advocate


def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_cost(route, coordinates):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return cost

def verify_solution(robot_tours, city_coordinates):
    # Requirement 1: Check if all tours start and end at the depot city (City 0)
    for tour_data in robot_tours:
        tour = tour_data['tour']
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
    # Requirement 2: Check if each city is visited exactly once and only the depot is visited more than once
    visited_cities = set()
    for tour_data in robot_tours:
        tour = tour_data['tour']
        for city in tour[1:-1]:  # Exclude the starting and ending depot entries
            if city in visited_cities:
                return "FAIL"
            visited_cily.add(city)
       
    if set(range(1, len(city_coordinates))) != visited_cities:
        return "FAIL" 
    
    # Verify each robot's tour cost
    overall_cost_calculated = 0
    for tour_data in robot_tours:
        tour = tour_data['tour']
        reported_cost = tour_data['cost']
        calculated_cost = total_route_cost(tour, city_coordinates)
        if not np.isclose(reported_cost, calculated_cost, atol=0.001):
            return "FAIL"
        overall_cost_calculated += reported_cost
    
    # Requirement 4: Check total travel cost consistency
    if not np.isclose(total_system_cost, overall_cost_calculated, atol=0.001):
        return "FAIL"
        
    return "CORRECT"

# Tours and costs alongside the city coordinates (must set these correctly as per the main execution context)
result = verify_solution(provided_tours, city_coordinates)
print(result)