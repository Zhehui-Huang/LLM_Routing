import math
from typing import List

# City coordinates
cities = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Tour and total provided by the solution
provided_tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
provided_cost = 410.04

def calculate_euclidean_distance(city1: int, city2: int) -> float:
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tour(tour: List[int], expected_cost: float) -> str:
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if every other city is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost and compare with expected cost
    total_calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not math.isclose(total_calculated_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Execute the validation function
result = validate_tour(provided_tour, provided_cost)
print(result)