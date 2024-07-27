import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Proposed tours and costs
robot_tours = {
    0: {"tour": [0, np.int64(4), np.int64(9), np.int64(14), np.int64(21), np.int64(19), 0], "cost": 181.62004235746448},
    1: {"tour": [1, np.int64(6), np.int64(17), np.int64(20), np.int64(18), np.int64(15), 1], "cost": 167.53540730006},
    2: {"tour": [2, np.int64(7), np.int64(10), np.int64(16), np.int64(8), 2], "cost": 123.25004226442609},
    3: {"tour": [3, np.int64(5), np.int64(12), np.int64(13), np.int64(11), 3], "cost": 131.82243372993375}
}
overall_cost = 604.2279256518843

# Function to calculate Euclidean distance between cities
def calculate_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Verify the solution
def verify_solution(robot_tours, cities, overall_cost):
    # Check if all cities are visited exactly once
    all_visited_cities = []
    total_calculated_cost = 0
    
    for robot, data in robot_tours.items():
        tour = data['tour']
        reported_cost = data['cost']
        calculated_cost = 0
        
        last_city = None
        for city in tour:
            if city in all_visited_cities and city not in [0, 1, 2, 3]:
                return "FAIL"
            all_visited_cities.append(city)
            
            if last_city is not None:
                calculated_cost += calculate_distance(last_city, city)
            
            last_city = city
        
        if abs(calculated_cost - reported_cost) > 1e-5:
            return "FAIL"
        
        total_calculated_cost += calculated_cost
    
    if len(set(all_visited_cities)) != 22 or total_calculated_cost != overall_cost:
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_solution(robot_tours, cities, overall_cost)
print(result)