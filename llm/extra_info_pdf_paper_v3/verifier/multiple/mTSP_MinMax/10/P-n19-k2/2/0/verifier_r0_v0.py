import numpy as np
from math import sqrt

# City coordinates including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided tours (transformed to zero-based index where necessary)
tours = [
    [0, 1, 10, 8, 16, 17, 3, 12, 14, 11, 4, 0],  # Robot 0
    [0, 6, 2, 7, 9, 15, 13, 5, 18, 0]  # Robot 1
]

# Provided travel costs
provided_costs = [116.32876651388246, 80.31749999965547]

def calculate_euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Validate all requirements
def validate_solution(tours, coords, provided_costs):
    visited_cities = set()
    all_costs = []

    # Requirement 1 and 2 validation
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Start or end not at depot
        for i in range(1, len(tour) - 1):
            visited_cities.add(tour[i])

        # Calculate cost
        cost = 0
        for j in range(len(tour) - 1):
            cost += calculate_euclidean_distance(coords[tour[j]], coords[tour[j + 1]])
        all_costs.append(cost)
        if not np.isclose(cost, provided_costs[tours.index(tour)], atol=0.0001):
            return "FAIL"  # Provided cost mismatch

    # Check if all cities except depot are visited exactly once
    if visited_cities != set(range(1, 19)):
        return "FAIL"

    # Requirement 3 is inherently validated by checking the max cost value
    if not np.isclose(max(all_costs), max(provided_costs), atol=0.0001):
        return "FAIL"

    return "CORRECT"

# Run the validation
result = validate_solution(tours, coordinates, provided_costs)
print(result)