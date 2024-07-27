import numpy as np

# Define the city coordinates
city_coords = {
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
    15: (37, 69)
}

# Define demands of each city
demands = {
    1: 19,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 31,
    7: 15,
    8: 28,
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11
}

# Define tours and calculate costs
robots_tours = {
    0: ([0, 9, 13, 15, 13, 0], 127.79),
    1: ([0, 3, 12, 0], 72.01)
    # Include all tours here to test all
}

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_tours(robots_tours, demands, city_coords):
    total_demand_fulfilled = {k: 0 for k in demands.keys()}
    total_cost_calculated = 0
    
    for robot, tour_data in robots_tours.items():
        tour, reported_cost = tour_data
        tour_cost = 0
        load = 0
        previous_city = tour[0]
        
        if previous_city != 0:
            return "FAIL: Tour must start and end at the depot (City 0)."
        
        for city in tour[1:]:
            if city != 0:
                load += demands.get(city, 0)
                demands[city] = max(0, demands[city] - demands.get(city, 0))
                
            distance = euclidean_distance(city_coords[previous_city], city_coords[city])
            tour_cost += distance
            previous_city = city
            
            if city == 0:
                if load > 35:
                    return f"FAIL: Robot load exceeded capacity of 35 on robot {robot}."
                load = 0
                
        if abs(tour_cost - reported_cost) > 1e-2:
            return f"FAIL: Reported cost and calculated cost do not match for Robot {robot}."
        
        total_cost_calculated += tour_cost
    
    for c, d in demands.items():
        if d > 0:
            return f"FAIL: Not all demands met. Remaining demand for city {c} is {d}."
    
    return "CORRECT"

result = verify_tours(robots_tours, demands, city_coords)
print(result)