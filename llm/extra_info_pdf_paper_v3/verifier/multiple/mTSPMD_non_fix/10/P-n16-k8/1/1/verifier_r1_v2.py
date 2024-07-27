import math

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

# Robot tours provided
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

# Verification function
def verify_solution():
    all_visited_cities = set()
    total_calculated_cost = 0.0

    for robot_id, tour in enumerate(robots_tours):
        # Verify tour starts and ends at the same point
        if tour[0] != tour[-1] or tour[0] != 0:
            return "FAIL"
        
        # Calculate and compare costs
        calculated_cost = 0.0
        for i in range(len(tour) - 1):
            distance = calculate_distance(tour[i], tour[i + 1])
            calculated_cost += distance

        if not math.isclose(calculated_cost, robots_costs[robot_id], rel_tol=1e-5):
            return "FAIL"

        all_visited_cities.update(tour[1:-1])  # Skip the depot city at start/end
        
        total_calculated_cost += calculated_cost

    if len(all_visited_cities) != len(cities) - 1: # Exclude the depot city
        return "FAIL"

    return "CORRECT"

# Execute the verification
print(verify_solution())