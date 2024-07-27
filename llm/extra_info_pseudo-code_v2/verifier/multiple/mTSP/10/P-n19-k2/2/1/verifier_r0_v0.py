import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

def verify_solution(robot_tours, city_coordinates):
    visited_cities = set()
    total_calculated_cost = 0
    for tour in robot_tours:
        start_city, end_city = tour[0], tour[-1]
        if start_city != 0 or end_city != 0:
            return "FAIL"  # Tours must start and end at the depot
        
        for city in tour:
            if not (0 <= city < len(city_coordinates)):
                return "FAIL"  # City indices must be within the correct range
        
        tour_cost = calculate_tour_cost(tour, city_coordinates)
        total_calculate_cost += tour_cost
        
        for city in tour[1:-1]:  # Exclude depot (start/end)
            visited_cities.add(city)
            
    if len(visited_cities) != len(city_coordinates) - 1:
        return "FAIL"  # Not all cities were visited exactly once
    
    if abs(total_calculated_cost - total_reported_cost) > 0.01:
        return "FAIL"  # The reported cost and the calculated cost do not match closely enough
    
    return "CORRECT"

# City coordinates including the depot
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Solution details from the user input
robot_tours = [
    [0, 6, 18, 5, 7, 2, 1, 10, 4, 11, 0],
    [0, 14, 12, 3, 8, 16, 17, 9, 15, 13, 0]
]

# Reported costs
tour_costs_reported = [107.16, 140.26]
total_reported_cost = 247.42

# Calculate costs for the provided tours
total_calculated_cost = sum(calculate_tour_cost(tour, city_codes) for tour, city_codes in zip(robot_tours, [city_coordinates, city_coordinates]))

# Check if costs approximately match
if abs(total_calculated_cost - total_reported_cost) <= 1e-2:
    print("CORRECT")
else:
    print("FAIL")