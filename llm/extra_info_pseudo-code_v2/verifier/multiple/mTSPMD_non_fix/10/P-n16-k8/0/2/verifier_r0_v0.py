import math

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Setting up dictionaries for city coordinates
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

# Unit Test Inputs
robot_tour = [0, 1, 1, 1, 1, 3, 3, 3, 3, 10, 10, 10, 2, 2, 2, 2, 2, 0]
expected_cost = 42.0460741407669
overall_cost = 42.0460741407669

# Function to validate the solution
def validate_solution():
    # Check if cities are visited exactly once, excluding the starting depot
    city_visit_count = {i: 0 for i in range(16)}
    for city in robot_tour:
        if city in city_visit_count:
            city_visit_count[city] += 1
    
    unique_visits = all(count == 1 for count in city_visit_count.values() if count > 0)
    
    # Calculate total travel cost
    total_travel_cost = 0
    for i in range(len(robot_tour) - 1):
        total_travel_cost += euclidean_distance(cities[robot_tour[i]], cities[robot_tour[i+1]])

    # Validate the costs
    cost_is_correct = math.isclose(total_travel_cost, expected_cost, rel_tol=1e-9)
    
    # Validate if start at depot 0 and do not need to return
    starts_at_depot = (robot_tour[0] == 0)
    ends_at_depot = (robot_tour[-1] == 0)

    # Combined all checks
    if unique_visits and cost_is_correct and starts_at_depot and ends_at_depot and math.isclose(total_travel_cost, overall_cost, rel_tol=1e-9):
        return "CORRECT"
    else:
        return "FAIL"

# Run the validation
print(validate_solution())