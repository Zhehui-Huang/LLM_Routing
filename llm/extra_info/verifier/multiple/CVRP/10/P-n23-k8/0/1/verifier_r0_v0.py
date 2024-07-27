import math

# City coordinates given as tuples, index corresponds to city number
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Demands for each city
city_demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26,
    17, 6, 15, 5, 10
]

# Proposed solution categorized by robot tours and travel costs
robot_tours = [
    ([0, 1, 2, 0], 47.28555690793142), ([0, 3, 4, 0], 75.67537984747364),
    ([0, 5, 6, 0], 47.93463581488838), ([0, 7, 0], 44.04543109109048),
    ([0, 8, 9, 0], 81.27545517717891), ([0, 11, 12, 10, 13, 0], 101.71935015146762),
    ([0, 14, 15, 0], 107.66099338871445), ([0, 16, 17, 0], 68.20018679138722),
    ([0, 20, 18, 19, 0], 98.5825948124361), ([0, 21, 22, 0], 52.491761791689186)
]

robot_capacity = 40
num_robots = 8

def calculate_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

def test_solution():
    total_delivered = [0] * len(city_demands)
    total_cost_calculated = 0
    
    if len(robot_tours) > num_robots:
        return "FAIL: More robots than available"
    
    for tour, reported_cost in robot_tours:
        start_city = tour[0]
        end_city = tour[-1]
        if start_city != 0 or end_city != 0:
            return "FAIL: Tour does not start or end at the depot"
        
        current_load = 0
        current_cost = 0
        prev_city = tour[0]
        
        for city in tour[1:]:
            demand = city_demands[city]
            current_load += demand
            total_delivered[city] += demand
            
            if current_load > robot_capacity:
                return "FAIL: Capacity exceeded"
            
            distance = calculate_distance(prev_city, city)
            current_cost += distance
            prev_city = city
        
        # round trip to the starting city
        current_cost += calculate_distance(prev_city, 0)
        
        if not math.isclose(current_cost, reported_cost, rel_tol=1e-5):
            return f"FAIL: Reported cost {reported_cost} does not match calculated cost {current_cost}"
        
        total_cost_calculated += current_cost
    
    if not all(city_demands[i] == total_delivered[i] for i in range(len(city_demands))):
        return "FAIL: Demand not fully met"
    
    return "CORRECT"

# Run the test function and print the result
print(test_solution())