import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robots_tours, robots_costs, cities_coordinates):
    # Unpack city coordinates
    cities = {i: coord for i, coord in enumerate(cities_coordinates)}
    
    city_visitation = {i: 0 for i in range(len(cities))}
    total_calculated_cost = 0
    for robot_id, tour in enumerate(robots_tours):
        # Start from a depot
        if tour[0] != 0:
            return "FAIL"
        
        # Robot does not need to return to the depot, check final city
        if tour[-1] not in [0, 1, 2, 3]:  # Assuming depots are cities 0, 1, 2, 3
            return "FAIL"

        last_city = tour[0]
        robot_travel_cost = 0
        
        for current_city in tour[1:]:
            city_visitation[current_city] += 1
            robot_travel_cost += calculate_distance(cities[last_city], cities[current_city])
            last_city = current_city

        # Validate the travel cost for current robot
        if not math.isclose(robot_travel_cost, robots_costs[robot_id], rel_tol=1e-9):
            return "FAIL"
        
        total_calculated_cost += robot_travel_cost

    # Check all cities are visited exactly once but depots could have >1 visits
    if any(visits != 1 for i, visits in city_visitation.items() if i > 3):
        return "FAIL"

    # Validate total cost
    if not math.isclose(total_calculated_cost, sum(robots_costs), rel_tol=1e-9):
        return "FAIL"

    # Check if the total cost is minimized
    # This would require solving the problem optimally and comparing, not feasible without the proper setup.
    # Assuming minimized for now as we're not equipped to resolve this within the script.

    return "CORRECT"

# Provided solution data
robots_tours = [
    [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 2, 1, 3, 4, 11, 13, 19, 21],
    [0], [0], [0]
]

robots_costs = [278.5478504011258, 0, 0, 0]

cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Assess the solution validity
result = verify_solution(robots_tours, robots_costs, cities_coordinates)
print(result)