import math
from collections import Counter

# Coordinates for each city index
coordinates = {
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Robots tour information
robots = {
    0: [0, 16, 0],
    1: [1, 10, 1]
}

def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tours(robots):
    all_visited_cities = []
    expected_cost = 34.142135624
    
    total_cost = 0
    for robot_id, tour in robots.items():
        depot = tour[0]
        tour_cost = 0
        
        # Check if tour starts and ends at its depot
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"
        
        # Calculate the tour cost
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            tour_cost += calculate_distance(city_from, city_to)
        
        all_visited_cities.extend(tour[1:-1])  # Exclude depots
        total_cost += tour_cost
    
    # Check if each city is visited exactly once
    city_count = Counter(all_visited_cities)
    if any(c != 1 for c in city_count.values()):
        return "FAIL"
    
    # Check if cost is minimized
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the test
test_result = check_tours(robots)
print(test_result)