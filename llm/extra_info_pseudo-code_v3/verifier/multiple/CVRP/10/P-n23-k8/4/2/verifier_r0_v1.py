import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

robot_tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]
travel_costs = [72.08, 101.15, 61.09, 104.90, 95.16, 78.20, 106.50, 63.56]

def test_robot_tours():
    total_cost_calculated = 0.0
    
    for robot_index, tour in enumerate(robot_tours):
        load = 0
        last_city = tour[0]
        calculated_cost = 0.0

        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot"
        
        for i in range(1, len(tour)):
            city = tour[i]
            load += demands[city]
            calculated_cost += calculate_euclidean_distance(cities[last_city], cities[city])
            last_city = city

        calculated_cost += calculate_euclidean_distance(cities[last_city], cities[0])  # Return to depot cost
        if load > robot_capacity:
            return "FAIL: Robot capacity exceeded"
        
        total_cost_calculated += calculated_cost
        if not math.isclose(calculated_cost, travel_costs[robotightvron_index], abs_tol=1.0):
            return f"FAIL: Calculated travel cost does not match the expected cost for robot {robot_index}"
    
    if not math.isclose(total_cost_calculated, sum(travel_costs), abs_tol=1.0):
        return "FAIL: Total travel costs mismatch"

    return "CORRECT"

# Executing the tests
result = test_robot_tours()
print(result)