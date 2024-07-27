import math

# Defined City Coordinates and Demands
cities = {
    0: {"coords": (145, 215), "demand": 0},
    1: {"coords": (151, 264), "demand": 1100},
    2: {"coords": (159, 261), "demand": 700},
    3: {"coords": (130, 254), "demand": 800},
    4: {"coords": (128, 252), "demand": 1400},
    5: {"coords": (163, 247), "demand": 2100},
    6: {"coords": (146, 246), "demand": 400},
    7: {"coords": (161, 242), "demand": 800},
    8: {"coords": (142, 239), "demand": 100},
    9: {"coords": (163, 236), "demand": 500},
    10: {"coords": (148, 232), "demand": 600},
    11: {"coords": (128, 231), "demand": 1200},
    12: {"coords": (156, 217), "demand": 1300},
    13: {"coords": (129, 214), "demand": 1300},
    14: {"coords": (146, 208), "demand": 300},
    15: {"coords": (164, 208), "demand": 900},
    16: {"coords": (141, 206), "demand": 2100},
    17: {"coords": (147, 193), "demand": 1000},
    18: {"coords": (164, 193), "demand": 900},
    19: {"coords": (129, 189), "demand": 2500},
    20: {"coords": (155, 185), "demand": 1800},
    21: {"coords": (139, 182), "demand": 700}
}

robot_capacity = 6000

# Tours and costs provided
robot_tours = [
    {"tour": [0, 1, 2, 0, 3, 4, 0, 18, 20, 0], "cost": 264.0586380420692},
    {"tour": [0, 5, 7, 0, 19, 21, 0], "cost": 149.7612442846346},
    {"tour": [0, 6, 8, 0, 9, 10, 0, 11, 13, 0, 15, 17, 0], "cost": 245.1272282323723},
    {"tour": [0, 14, 16, 0], "cost": 22.305090420796084}
]

expected_total_cost = 681.2522009798722

def calculate_distance(city1, city2):
    coord1 = cities[city1]['coords']
    coord2 = cities[city2]['coords']
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tours):
    total_cost_computed = 0
    demands_met = [0] * len(cities)
    
    for robot in tours:
        route = robot['tour']
        load = 0
        last_city = route[0]
        accumulated_cost = 0
        
        for city in route[1:]:
            if city != 0:  # Do not count start/end depot city demand
                demands_met[city] += cities[city]['demand']
                load += cities[city]['demand']
                
            # Calculate travel cost
            distance = calculate_distance(last_city, city)
            accumulated_cost += distance
            last_city = city
            
            if load > robot_capacity:
                return "FAIL: Capacity exceeded"
        
        # Check if calculated cost and provided cost are almost equal
        if not math.isclose(accumulated_cost, robot['cost'], abs_tol=1e-4):
            return "FAIL: Travel cost mismatch"
        
        total_cost_computed += accumulated_cost
    
    if not math.isclose(total_cost_computed, expected_total_collected, abs_tol=1e-4):
        return "FAIL: Total cost mismatch"
    
    if any(d != cities[i]['demand'] for i, d in enumerate(demands_met)):
        return "FAIL: Demand not fully met"
    
    return "CORRECT"

# Perform the verification
result = verify_solution(robot_tours)
print(result)