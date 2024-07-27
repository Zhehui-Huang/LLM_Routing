import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(route, total_distance, cities_coords):
    if len(route) != 21:
        return "FAIL"
    
    if set(route) != set(range(21)):
        return "FAIL"
    
    if route[0] != 0 or route[-1] != 1:
        return "FAIL"
    
    calculated_total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        x1, y1 = cities_coords[city1]
        x2, y2 = cities_coords[city2]
        calculated_total_distance += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if abs(calculated_total_distance - total_distance) > 1e-6:
        return "FAIL"
    
    # Check depots are utilized properly (additional validation; actually checked implicitly above)
    existence_robot_depot = route[0] == 0 and any(r == 1 for r in route[1:])
    if existence_robot_depot:
        pass # Valid configuration
    else:
        return "FAIL"
    
    return "CORRECT"

cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

route_solution = [0, 4, 11, 15, 12, 10, 2, 20, 5, 14, 17, 9, 18, 19, 3, 8, 13, 7, 6, 16, 1]
total_distance_solution = 201.10883561044764

# Perform the verification.
result = verify_solution(route_solution, total_distance_solution, cities_coordinates)
print(result)