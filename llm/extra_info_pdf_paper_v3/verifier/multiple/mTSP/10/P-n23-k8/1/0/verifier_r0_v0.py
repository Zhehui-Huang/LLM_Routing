import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_cost(route, coordinates):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return cost

def verify_solution(robot_tours, city_coordinates):
    # Requirement 1: Check if all tours start and end at the depot city (City 0)
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
    # Requirement 2: Check if each city is visited exactly once and only the depot is visited more than once
    visited_cities = set()
    for tour in robot_tours:
        for city in tour[1:-1]:  # Exclude the starting and ending depot entries
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
    
    # Check if all cities except the depot (0) are visited
    if set(range(1, len(city_coordinates))) != visited_cities:
        return "FAIL"
    
    # Check each robot's tour cost and overall cost
    overall_cost_calculated = 0
    for tour in robot_tours:
        calculated_cost = total_route_cost(tour, city_coordinates)
        reported_cost = tour['cost']
        if not np.isclose(reported_cost, calculated_cost, atol=0.001):
            return "FAIL"
        overall_cost_calculated += reported_cost
    
    # Requirement 4: Check total travel cost consistency (cumulatively from all robots)
    if not np.isclose(total_system_cost, overall_cost_calculated, atol=0.001):
        return "FAIL"
        
    return "CORRECT"

# Define city coordinates
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
                    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
                    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
                    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
                    (45, 35), (32, 39), (56, 37)]

provided_tours = [
    {'tour': [0, 1, 9, 17, 0], 'cost': 81.65415032740114},
    {'tour': [0, 2, 18, 10, 0], 'cost': 81.81803428067735},
    {'tour': [0, 3, 19, 11, 0], 'cost': 108.81482905718964},
    {'tour': [0, 4, 12, 20, 0], 'cost': 82.89654293014993},
    {'tour': [0, 13, 5, 21, 0], 'cost': 68.39261497384648},
    {'tour': [0, 6, 22, 14, 0], 'cost': 67.67055146540517},
    {'tour': [0, 7, 15, 0], 'cost': 83.62034367443502},
    {'tour': [0, 16, 8, 0], 'cost': 64.92216653342012}
]

# Total system cost reported
total_system_cost = 639.7892332425249

# Verify the solution
result = verify_solution(provided_tours, city_coordinates)
print(result)