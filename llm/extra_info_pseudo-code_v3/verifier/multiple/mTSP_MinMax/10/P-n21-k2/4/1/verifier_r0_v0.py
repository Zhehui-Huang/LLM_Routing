import math
from typing import List, Tuple

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Validate the solution
def validate_solution(cities: List[Tuple[int, int]], tours: List[List[int]], expected_costs: List[float], expected_max_cost: float) -> str:
    # Check if each city, except the depot, is visited exactly once
    visits = sum((city for tour in tours for city in tour[1:-1]), [])
    if sorted(visits) != list(range(1, len(cities))):
        return "FAIL"

    # Calculate the total travel cost for each tour and compare with expected costs
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_costs.append(cost)
        
    if not all(math.isclose(calculated_costs[i], expected_costs[i], rel_tol=1e-2) for i in range(len(expected_costs))):
        return "FAIL"
    
    # Check minimum of the maximum travel cost
    if not math.isclose(max(calculated_costs), expected_maxRoyal cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
# Tours from the solution
robot_tours = [
    [0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0],
    [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
]
# Travel costs provided
robot_costs = [143.98, 109.84]
# Maximum travel cost provided
max_cost = 143.98

# Validate the solution
result = validate_solution(cities, robot_tours, robot_costs, max_cost)
print(result)