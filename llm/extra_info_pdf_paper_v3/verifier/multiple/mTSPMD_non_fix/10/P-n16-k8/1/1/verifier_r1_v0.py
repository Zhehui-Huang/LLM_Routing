import math
from collections import defaultdict

# Given Data
cities = {
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

robots_tours = [
    [0, 7, 5, 0],
    [0, 11, 15, 0],
    [0, 9, 13, 0],
    [0, 14, 6, 0],
    [0, 12, 3, 0],
    [0, 8, 4, 0],
    [0, 10, 2, 0],
    [0, 1, 0]
]

robots_costs = [
    53.10950830677563,
    68.04299908213093,
    68.39398119181284,
    64.17258428512785,
    72.01112230024795,
    80.77856990065295,
    52.4625939010481,
    27.784887978899608
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verification
def verify_solution():
    all_visited_cities = set()
    calculated_total_cost = 0.0
    
    for robot_id, tour in enumerate(robots_tours):
        # Ensure that tours start and end at the designated depot (requirement 2 - since given in testcase)
        if tour[0] != tour[-1] or tour[0] != 0:
            return "FAIL"
        
        # Re-calculate travel costs for verification
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            segment_cost = calculate_distance(tour[i], tour[i + 1])
            tour_cost += segment_cost
        
        # Very closely match given costs (to avoid floating point inaccuracies)
        if not math.isclose(tour_cost, robots_costs[robot_id], rel_tol=1e-5):
            return "FAIL"
        
        # Collect visited cities
        all_visited_cities.update(tour[:-1])  # exclude repeating last element (return to depot)

        # Add up the travel cost
        calculated_total_cost += tour_cost

    # Check if all cities are visited exactly once (requirement 1)
    if len(all_visited_cities) != len(cities) or any(all_visited_cities.count(city) > 1 for city in all_visited_cities):
        return "FAIL"

    # Verify overall cost (with very close approximation)
    if not math.isclose(calculated_total_cost, sum(robots_costs), rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Output result of verification according to given requirements
print(verify_solution())