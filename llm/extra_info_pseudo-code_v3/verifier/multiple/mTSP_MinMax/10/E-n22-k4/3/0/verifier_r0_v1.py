import math

# City coordinates
coordinates = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Tours provided
tours = [
    [0, 12, 14, 15, 16, 18, 0],
    [0, 3, 4, 6, 8, 10, 11, 0],
    [0, 13, 17, 19, 20, 21, 0],
    [0, 1, 2, 5, 7, 9, 0]
]

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def validate_solution(tours):
    cities_visited = set()
    robot_costs = []
    
    for tour in tours:
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate cost of each tour and collect visited cities
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i + 1])
            if i > 0:  # Exclude the depot from unique visitation checks
                cities_visited.add(tour[i])
                
        robot_costs.append(tour_cost)
    
    # Check if all cities except the depot are visited exactly once
    if len(cities_visited) != 21 or not cities_visited == set(range(1, 22)):
        return "FAIL"

    # Check if the maximum cost is minimized
    max_cost = max(robot_costs)
    if max_cost > min(robot_costs) * 1.20:  # Assuming an acceptable distribution, tweakable threshold
        return "FAIL"
    
    return "CORRECT"

# Output the validation result
print(validate_solution(tours))