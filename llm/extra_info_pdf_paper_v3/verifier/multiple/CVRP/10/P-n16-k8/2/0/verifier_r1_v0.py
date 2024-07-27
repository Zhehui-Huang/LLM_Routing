import math

# Data provided
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31,
    7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14,
    13: 6, 14: 19, 15: 11
}
robot_capacity = 35

# Robot tours provided in the solution
robot_tours = {
    0: [0, 1, 0],
    1: [0, 2, 0],
    2: [0, 3, 0],
    3: [0, 4, 5, 0],
    4: [0, 6, 0],
    5: [0, 7, 0],
    6: [0, 8, 0],
    7: [0, 9, 10, 11, 0]
}

# Calculate distances
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Verify requirements
def verify_solution():
    global cities, demands, robot_capacity, robot_tours
    
    # A set to keep track of all visited cities except depot
    all_visited_cities = set()
    
    for r, tour in robot_tours.items():
        total_load = 0
        prev_city = tour[0]
        
        for city in tour[1:]:
            # Check if start and end point are depot
            if tour[0] != 0 or tour[-1] != 0:
                return "FAIL"
            
            if city != 0:
                # Capacity Check
                total_load += demands.get(city, 0)
                # Mark the city as visited
                all_visited_cities.add(city)
            
            prev_city = city
        
        if total_load > robot_capacity:
            return "FAIL"
    
    # Check all cities with demands are visited
    if not all(c in all_visited_cities for c in demands):
        return "FAIL"
    
    return "CORRECT"

result = verify_solution()
print(result)