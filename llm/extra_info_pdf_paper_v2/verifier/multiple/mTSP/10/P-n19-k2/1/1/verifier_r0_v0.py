import math

# Define the city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Provided tours and travel costs
robot_tours = [
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0],
    [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
]
provided_costs = [143.98241284438606, 97.30815163794452]

# Required validations
def validate_solution():
    all_visited_cities = set()
    total_calculated_cost = 0

    for robot_index, tour in enumerate(robot_tours):
        # Check if tours start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate the tour cost and check tour validity
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
            all_visited_cities.add(tour[i])
        
        all_visited_cities.add(tour[-1])  # add the last city in the loop
        
        # Compare calculated cost with provided cost
        if not math.isclose(tour_cost, provided_costs[robot_index], rel_tol=1e-5):
            return "FAIL"
        
        total_calculated_cost += tour_cost
    
    # Check if all cities except the depot are visited exactly once
    if all_visited_cities != set(range(19)):
        return "FAIL"
    
    # Check if total cost matches the provided total
    expected_total_cost = sum(provided_costs)
    if not math.isclose(total_calculated_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the validation
result = validate_solution()
print(result)