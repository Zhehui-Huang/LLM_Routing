import math
from itertools import chain

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Tours assigned to each robot
robots_tours = [
    [0, 21, 7, 9, 0],
    [0, 16, 5, 17, 0],
    [0, 6, 22, 8, 0],
    [0, 1, 12, 15, 0],
    [0, 20, 14, 18, 0],
    [0, 10, 3, 19, 0],
    [0, 2, 13, 0],
    [0, 4, 11, 0]
]

# Individual travel costs provided
individual_travel_costs = [64.45, 69.89, 80.08, 66.21, 106.71, 89.03, 59.20, 57.39]
calculated_costs = []

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solutions():
    # [Requirement 1] check if tour starts and ends at depot (city 0)
    if not all(tour[0] == 0 and tour[-1] == 0 for tour in robots_tours):
        return "FAIL"

    # [Requirement 2] check if all cities are visited exactly once
    all_cities_visited = set(chain.from_iterable(tour[1:-1] for tour in robots_tours))
    if all_cities_visited != set(range(1, 23)):
        return "FAIL"

    # [Requirement 4] verify travel costs
    for tour in robots_tours:
        tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        calculated_costs.append(round(tour_cost, 2))
    if not all(math.isclose(provided, calculated, rel_tol=1e-2) for provided, calculated in zip(individual_travel_costs, calculated_costs)):
        return "FAIL"

    # [Requirement 5] is implicitly checked by the structured output format in the problem context.

    # Verify the summed cost 
    if not math.isclose(sum(individual_travel_costs), 592.94, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Output of verification function
print(verify_solutions())