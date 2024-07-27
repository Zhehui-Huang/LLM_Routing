import math

# Define a helper function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Define cities' coordinates
city_coords = {
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
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Robot tours and expected costs provided
robot_tours = [
    [0, 16, 10, 1, 0],
    [0, 2, 7, 22, 5, 0],
    [0, 8, 18, 19, 3, 0],
    [0, 15, 12, 0],
    [0, 17, 14, 0],
    [0, 21, 20, 6, 0],
    [0, 13, 9, 0],
    [0, 11, 4, 0]
]

expected_costs = [
    42.6682117120349,
    63.968301047161326,
    90.24447898713359,
    66.12407122823275,
    69.35939917750704,
    34.587336997526904,
    68.39398119181286,
    57.394073777130664
]

expected_max_cost = 90.24447898713359

def verify_solution(robot_tours, expected_costs, expected_max_cost):
    correct = True
    
    # Check requirements
    visited_cities = set()
    max_cost_found = 0

    for tour, expected_cost in zip(robot_tours, expected_costs):
        tour_cost = 0
        for i in range(len(tour) - 1):
            distance = calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
            tour_cost += distance
            visited_cities.add(tour[i])
        
        # Requirement 4: Check if tour start and end at depot and track cities
        if tour[0] != 0 or tour[-1] != 0:
            correct = False
        
        # Requirement 5: Check computed and expected cost
        if not math.isclose(tour_cost, expected_cost, rel_tol=1e-9):
            correct = False

        # Update maximum cost
        if tour_cost > max_cost_found:
            max_cost_found = tour_cost

    # Requirement 1: Check if all cities visited exactly once
    if visited_cities != set(city_coords.keys()):
        correct = False

    # Requirement 6: Check maximum cost
    if not math.isclose(max_cost_found, expected_max_cost, rel_tol=1e-9):
        correct = False
    
    return "CORRECT" if correct else "FAIL"

# Execute the verification
result = verify_solution(robot_tours, expected_costs, expected_max_cost)
print(result)