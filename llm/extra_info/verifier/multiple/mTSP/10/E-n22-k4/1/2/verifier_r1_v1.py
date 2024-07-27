import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities_coordinates, robot_tours, expected_costs):
    city_count = len(cities_coordinates)
    num_robots = len(robot_tours)
    city_visits = [False] * city_count
    calculated_costs = []
    total_travel_cost = 0
    
    # Validate each robot's tour
    for i in range(num_robots):
        robot_tour = robot_tours[i]
        last_city_index = 0
        tour_cost = 0
        
        if robot_tour[0] != 0 or robot_tour[-1] != 0:
            return "FAIL: Tour must start and end at depot"

        for city_index in robot_tour[1:-1]:
            if city_visits[city_index]:
                return "FAIL: City visited more than once"
            city_visits[city_index] = True
            tour_cost += calculate_distance(cities_coordinates[last_city_index], cities_coordinates[city_index])
            last_city_index = city_index
        tour_cost += calculate_distance(cities_coordinates[last_city_index], cities_coordinates[0])
        
        calculated_costs.append(tour_cost)
        total_travel_cost += tour_cost
        
        if not abs(tour_cost - expected_costs[i]) < 1e-5:
            return f"FAIL: Incorrect travel cost calculation for Robot {i}: expected {expected_costs[i]}, got {tour_cost}"
        
    # Check if all cities were visited exactly once
    if not all(city_visits[1:]):
        return "FAIL: Not all cities were visited exactly once"
    
    if not abs(total_travel_cost - sum(expected_costs)) < 1e-5:
        return "FAIL: Overall travel cost incorrect"
    
    return "CORRECT"

# Providing the test cases and expected results

cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

robot_tours = [
    [0, 14, 16, 12, 15, 18, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 13, 19, 21, 17, 20, 0],
    [0, 9, 7, 5, 2, 1, 0]
]

expected_costs = [
    87.16778614302781,
    99.60668471182551,
    109.77573076701911,
    111.83855721201843
]

print(verify_solution(cities_coordinates, robot_tours, expected_costs))