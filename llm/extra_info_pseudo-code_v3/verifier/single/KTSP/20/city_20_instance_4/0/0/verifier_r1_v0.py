import math
from typing import List, Tuple

def euclidean_distance(pt1: Tuple[int, int], pt2: Tuple[int, int]) -> float:
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def verify_tour(tour: List[int], total_cost: float, cities_coordinates: List[Tuple[int, int]]) -> str:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(tour) != 17:  # 16 cities + return to depot
        return "FAIL"
    
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # Calculate the distance from the tour
    computed_total_distance = 0.0
    for i in range(len(tour) - 1):
        computed_total_distance += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
    
    # Check if computed distance is close to the given total due to floating point arithmetic issues
    if not math.isclose(computed_total_distance, total_score, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Tour and total travel cost provided in the solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 12, 6, 3, 15, 10, 0]
total_score = 307.6692

# Verification
result = verify_tour(tour, total_score, cities_coordinates)
print(result)