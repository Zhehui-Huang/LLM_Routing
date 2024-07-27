import numpy as np
from scipy.spatial.distance import euclidean

# Define the solution
robot_tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 0],
    [0, 4, 0],
    [0, 11, 0],
    [0, 15, 0],
    [0, 12, 0],
    [0, 8, 0],
    [0, 3, 0],
    [0]
]

# Travel cost claims
costs_claimed = [
    101.91119595240622,
    44.04543109109048,
    56.32051136131489,
    59.665735560705194,
    59.93329625508679,
    64.89992295835181,
    65.11528238439882,
    0
]

overall_cost_claimed = 451.89137556335413

# City coordinates indexed by city number
city_coordinates = {
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
}

def compute_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_cost

# Check if tours start at designated depot (city 0)
starts_from_depot = all(tour[0] == 0 for tour in robot_tours)

# Check if all cities are visited exactly once
all_cities = set(range(16))
visited_cities = set(city for tour in robot_tours for city in tour)
all_visited_once = visited_cities == all_cities

# Check claimed costs
costs_computed = [compute_cost(tour) for tour in robot_tours]
costs_match_claimed = np.isclose(costs_computed, costs_claimed, atol=1e-2)

# Check overall cost
total_computed_cost = sum(costs_computed)
overall_cost_match = np.isclose(total_computed_cost, overall_cost_claimed, atol=1e-2)

# Final verification of solution correctness
if starts_from_depot and all_visited_once and all(costs_match_claimed) and overall_cost_match:
    print("CORRECT")
else:
    print("FAIL")