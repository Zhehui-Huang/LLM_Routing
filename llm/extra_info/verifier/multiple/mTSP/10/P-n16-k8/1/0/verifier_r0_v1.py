import math
from itertools import chain

# City coordinates provided, including the depot
city_coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # City 1
    (49, 49),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 48),  # City 13
    (58, 27),  # City 14
    (37, 69)   # City 15
]

# Given robot tours and travel costs (Presented solution)
robot_tours = [
    [0, 6, 0],
    [0, 15, 12, 0],
    [0, 14, 0],
    [0, 2, 13, 9, 0],
    [0, 4, 11, 0],
    [0, 8, 3, 0],
    [0, 1, 10, 0],
    [0, 7, 5, 0]
]

# Expected costs provided for each tour by robots
expected_costs = [
    24.08318915758459,
    66.12407122823275,
    61.741396161732524,
    69.35272281445683,
    57.394073777130664,
    72.81785234728197,
    41.77216384800009,
    53.10950830677563
]

def calculate_distance(city_a, city_b):
    """ Calculate Euclidean distance between two cities given their indices. """
    x1, y1 = city_coordinates[city_a]
    x2, y2 = city_coordinates[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tours():
    """ Validating the tours based on the requirements. """
    all_cities_visited = list(chain.from_iterable(tour[1:-1] for tour in robot_tours))
    all_cities_visited_unique = len(set(all_cities_visited)) == 15  # 15 cities apart from the depot
    
    # Check requirement 2 - Each robot can visit each city exactly once, except for the depot
    if not all_cities_visited_unique or len(all_cities_visited) != 15:
        return "FAIL"
    
    # Check requirement 1 - All robots must start and end their tour at the depot city (city 0)
    if any(tour[0] != 0 or tour[-1] != 0 for tour in robot_tours):
        return "FAIL"
    
    # Calculate and verify individual and overall costs
    calculated_costs = []
    for tour in robot_tours:
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        calculated_costs.append(tour_cost)
    
    # Close to expected due to floating point operations, tolerance needed:
    if any(not math.isclose(calculated_costs[i], expected_costs[i], rel_tol=1e-9) for i in range(len(robot_tours))):
        return "FAIL"
    
    total_cost = sum(calculated_costs)
    expected_total_cost = sum(expected_costs)
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the validation function
result = validate_tours()
print(result)