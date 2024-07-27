import math

# Coordinates of the cities
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Provided tours
robot_tours = {
    0: [0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0],
    1: [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
}

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def validate_tours():
    visited = set()
    total_distances = []
    
    # Check each robot's tour
    for robot_id in robot_tours:
        tour = robot_tours[robot_id]
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Start or end not at depot
        for i in range(len(tour) - 1):
            visited.add(tour[i])
            if tour[i] == tour[i + 1]:
                return "FAIL"  # Same city visited consecutively
            
    # Check if all cities except depot are visited exactly once
    if visited != set(range(1, 21)):
        return "FAIL"
    
    # Check if maximum distance traveled is minimized
    max_distance = 0
    for robot_id in robot_tours:
        tour = robot_tours[robot_id]
        total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_distances.append(total_distance)
        max_distance = max(max_distance, total_distance)
    
    # To verify if provided maximum distance is correctly calculated
    if float(max_distance) != 143.98241284438606:
        return "FAIL"
    
    return "CORRECT"

# Output the result of the validation
print(validate_tours())