import math
from typing import List, Tuple

def euclidean_distance(pt1: Tuple[int, int], pt2: Tuple[int, int]) -> float:
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def check_requirements(tour: List[int], positions: List[Tuple[int, int]]) -> str:
    # Check [Requirement 1]: Start and end at depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check [Requirement 2]: Each city visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(positions) or min(unique_cities) != 0 or max(unique_cities) != len(positions) - 1:
        return "FAIL"
    
    # No need to validate [Requirement 3] as it's a target to optimize and not a constraint to check with true or false

    return "CORRECT"

# Input data for cities
city_positions = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Solution provided
solution_tour = [0, 8, 10, 1, 11, 9, 4, 7, 3, 5, 6, 2, 13, 14, 12, 0]
calculated_max_distance = 72.24956747275377

# Calculate maximum distance between consecutive cities in the proposed tour
max_distance = 0
total_travel_cost = 0
for i in range(len(solution_tour) - 1):
    dist = euclidean_distance(city_positions[solution_tour[i]], city_positions[solution_tour[i + 1]])
    total_travel_cost += dist
    if dist > max_distance:
        max_distance = dist

# Print the result of the test
result = check_requirements(solution_tour, city_positions)
if result == "CORRECT" and abs(max_distance - calculated_max_record) < 1e-6:
    print("CORRECT")
else:
    print("FAIL")