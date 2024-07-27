import math

# Data for cities' coordinates and demands
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

demand_list = {
    1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15,
    8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19,
    15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10
}

robot_tours = {
    0: ([0, 19, 18, 3, 0], 92.62),
    1: ([0, 8, 9, 0], 81.28),
    2: ([0, 17, 13, 11, 0], 112.13),
    3: ([0, 14, 12, 1, 0], 103.64),
    4: ([0, 15, 22, 5, 10, 0], 119.51),
    5: ([0, 7, 4, 0], 73.74),
    6: ([0, 2, 21, 0], 42.98),
    7: ([0, 20, 6, 0], 34.56)
}

def calculate_euclidean_distance(city_a, city_b):
    xa, ya = cities_coordinates[city_a]
    xb, yb = cities_coordinates[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

def verify_solution():
    total_reported_cost = 0
    total_demands_fulfilled = {k: 0 for k in demand_list.keys()}
    
    for robot_id, (tour, reported_cost) in robot_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot"
        
        calculated_cost = 0.0
        load = 0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            
            if city_to != 0:  # Depot city demand is zero and should not be counted
                load += demand_list.get(city_to, 0)
                total_demands_fulfilled[city_to] += demand_list.get(city_to, 0)
            
            calculated_cost += calculate_euclidean_distance(city_from, city_to)
        
        if load > 40:
            return f"FAIL: Capacity exceeded for robot {robot_id}"

        if abs(reported_cost - calculated_cost) > 0.01:  # Allow minor discrepancies
            print(f"Cost mismatch for Robot {robot_id}: reported {reported_cost}, calculated {calculated_cost}")
            return "FAIL"
    
    if any(total_demands_fulfilled[city] != demand_list[city] for city in demand_list):
        return "FAIL: Demands not properly fulfilled"
    
    return "CORRECT"

result = verify_solution()
print(result)