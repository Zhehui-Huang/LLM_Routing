import math
from typing import List, Tuple

def calculate_euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tsp_solution(tour: List[int], total_cost: float, coordinates: List[Tuple[int, int]]) -> str:
    # Requirement 1: Route must start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Robot must visit exactly 16 cities, including the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 16 or len(tour) != 17:
        return "FAIL"
    
    # Requirement 3 and 4: Calculate the travel cost; ensure it matches the given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_euclidean_distance(coordinates[city1], coordinates[city2])
    
    calculated_cost = round(calculated_cost, 2)
    
    # Requirement 5: Check the total travel cost is close enough to the given 
    if abs(calculated_cost - total_cost) > 0.001:
        return "FAIL"
    
    return "CORRECT"
  
# Cities coordinates indexed from 0 to 19
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided solution tour and travel cost
tour = [0, 12, 7, 16, 14, 11, 13, 1, 19, 8, 9, 10, 6, 3, 4, 15, 0]
total_cost = 434.32

# Perform validation
result = verify_tsp_solution(tour, total_cost, coordinates)
print(result)