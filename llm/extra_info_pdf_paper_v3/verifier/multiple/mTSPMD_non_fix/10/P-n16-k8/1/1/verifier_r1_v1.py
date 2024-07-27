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
    x1, y = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verification function
def verify_solution():
    all_visited_cities = defaultdict(int)
    calculated_total_cost = 0.0
    
    for robot_id, tour in enumerate(robots_tours):
        # Check if tour starts and ends at the same point (return to depot)
        if tour[0] != tour[-1] or tour[0] != 0:
            return "FAIL"

        # Calculate travel costs and update city visits
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            segment_cost = calculate_distance(tour[i], tour[i + 1])
            tour_cost += segment_cost
            all_visited_cities[tour[i]] += 1

        # Round off the tour cost to match the provided accuracy before comparing
        if not math.isclose(tour_cost, robots_costs[robot_id], rel_tol=1e-5):
            return "FAIL"
        
        all_visited_cities[tour[-1]] += 1  # count final city only once as it is start/end point

        # Sum total costs
        calculated_total_cost += tour_cost

    # The last city in each tour is the return to the depot, not a separate visit
    if len(all_visited_cities) != len(cities) or any(count != 2 for count in all_visited_cities.values()):
        return "FAIL"

    # Check the cumulative cost
    if not math.isright(calculated_total_cost, sum(robots_costs), rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute the test
print(verify_solution())