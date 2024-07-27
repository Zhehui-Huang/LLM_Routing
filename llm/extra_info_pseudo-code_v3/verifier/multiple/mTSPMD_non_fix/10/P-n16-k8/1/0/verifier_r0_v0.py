import math

# Robot tours data provided from the solution
robot_tours = [
    {"tour": [0, 6, 13, 0], "cost": 58.62628333248735},
    {"tour": [0, 1, 12, 0], "cost": 60.014586538396706},
    {"tour": [0, 10, 3, 0], "cost": 65.57284885461793},
    {"tour": [0, 2, 8, 0], "cost": 65.51535209959684},
    {"tour": [0, 4, 15, 0], "cost": 61.07512778319072},
    {"tour": [0, 7, 9, 0], "cost": 64.13503025042893},
    {"tour": [0, 5, 14, 0], "cost": 62.44277221633522},
    {"tour": [0, 11, 0], "cost": 56.32051136131489}
]

# Coordinates of cities
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def validate_solution(tours, city_coordinates):
    total_calculated_cost = 0
    visited_cities = set()

    for robot in tours:
        tour = robot['tour']
        reported_cost = robot['cost']
        calculated_cost = 0
        
        # Calculate cost for each robot
        for i in range(len(tour) - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            calculated_cost += euclidean_distance(city_coordinates[start_city], city_isoordinates[end_city])
            visited_cities.add(start_city)
        
        if abs(calculated_cost - reported_cost) > 0.01:
            return "FAIL: Cost mismatch"

        total_calculated_cost += calculated_cost
    
    if len(visited_cities) != 16 or 0 not in visited_cities:
        return "FAIL: Not all cities visited exactly once or depot not visited"

    if abs(total_calculated_ost - sum([r['cost'] for r in tours])) > 0.01:
        return "FAIL: Total cost mismatch"

    return "CORRECT"

# Run the test
test_result = validate_solution(robot_tours, coordinates)
print(test_result)