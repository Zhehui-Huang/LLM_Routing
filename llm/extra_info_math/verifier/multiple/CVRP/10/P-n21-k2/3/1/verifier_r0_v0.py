import math

def calculate_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Demands for each city
demands = {
    0: 0, 
    1: 7, 
    2: 30, 
    3: 16, 
    4: 23, 
    5: 11, 
    6: 19, 
    7: 15,
    8: 28, 
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11,
    16: 12,
    17: 26,
    18: 17,
    19: 6,
    20: 15
}

# Tours and claimed travel costs
robots_tours = {
    0: {"tour": [0, 6, 0], "cost": 24.08},
    1: {"tour": [0, 16, 0], "cost": 20.00}
}

# Check constraints
def check_solution(robots_tours, demands, cities):
    visited_cities = set()
    total_cost_calculated = 0
    robot_capacity = 160

    for robot_id, data in robots_tours.items():
        tour = data["tour"]
        reported_cost = data["cost"]
        
        # Check if each route starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate total demand and validate against robot's capacity
        total_demand = sum(demands[city] for city in tour if city in demands)
        if total_demand > robot_capacity:
            return "FAIL"
        
        # Calculate travel cost and compare it against reported cost
        calc_cost = 0
        for i in range(len(tour) - 1):
            calc_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        
        if not math.isclose(calc_cost, reported_cost, abs_tol=0.01):  # Allowing some tolerance
            return "FAIL"
        
        # Record visited cities
        visited_cities.update(tour[1:-1])

        # Accumulate overall cost
        total_cost_calculated += calc_cost
    
    # Check if each city (excluding the depot) is visited exactly once
    if visited_cities != set(cities.keys()) - {0}:
        return "FAIL"
    
    # Check total cost
    if not math.isclose(total_cost_calculated, 44.08, abs_tol=0.01):  # Allowing some tolerance on total costs
        return "FAIL"

    return "CORRECT"

# Execute verification function
result = check_solution(robots_tours, demands, cities)
print(result)