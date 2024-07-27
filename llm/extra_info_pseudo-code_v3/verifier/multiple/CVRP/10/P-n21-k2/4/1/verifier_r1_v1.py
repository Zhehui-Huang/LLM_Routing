import math

# Definition of cities, their coordinates and demands
cities = {
    0: {'coords': (30, 40), 'demand': 0},
    1: {'coords': (37, 52), 'demand': 7},
    2: {'coords': (49, 49), 'demand': 30},
    3: {'coords': (52, 64), 'demand': 16},
    4: {'coords': (31, 62), 'demand': 23},
    5: {'coords': (52, 33), 'demand': 11},
    6: {'coords': (42, 41), 'demand': 19},
    7: {'coords': (52, 41), 'demand': 15},
    8: {'coords': (57, 58), 'demand': 28},
    9: {'coords': (62, 42), 'demand': 8},
    10: {'coords': (42, 57), 'demand': 8},
    11: {'coords': (27, 68), 'demand': 7},
    12: {'coords': (43, 67), 'demand': 14},
    13: {'coords': (58, 48), 'demand': 6},
    14: {'coords': (58, 27), 'demand': 19},
    15: {'coords': (37, 69), 'demand': 11},
    16: {'coords': (38, 46), 'demand': 12},
    17: {'coords': (61, 33), 'demand': 26},
    18: {'coords': (62, 63), 'demand': 17},
    19: {'coords': (63, 69), 'demand': 6},
    20: {'coords': (45, 35), 'demand': 15}
}

robot_tours = {
    0: ([0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0], 135.57),
    1: ([0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0], 160.83)
}

robot_capacity = 160

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]['coords']
    x2, y2 = cities[city2]['coords']
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution():
    total_cost_calculated = 0.0
    for robot_id, tour_info in robot_tours.items():
        tour, reported_cost = tour_info
        current_load = 0
        calculated_cost = 0.0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            calculated_cost += calculate_distance(city_from, city_to)
            if city_to != 0:
                current_load += cities[city_to]['demand']
        
        if current_load > robot_capacity:
            return f"FAIL: Capacity exceeded for Robot {robot_id}"
        
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
            return f"FAIL: Incorrect cost for Robot {robot_id}. Expected {calculated_cost}, got {reported_burse
        total_cost_calculated += calculated_cost
    
    if not math.isclose(total_cost_calculated, 296.40, rel_tol=1e-2):
        return f"FAIL: Incorrect total travel cost. Expected 296.40, got {total_cost_calculated}"
    
    visited = [city for tour in robot_tours.values() for city in tour[0][1:-1]]
    if sorted(visited) != list(range(1, 21)):
        return "FAIL: Not all cities visited or some cities visited more than once"

    return "CORRECT"

result = verify_solution()
print(result)