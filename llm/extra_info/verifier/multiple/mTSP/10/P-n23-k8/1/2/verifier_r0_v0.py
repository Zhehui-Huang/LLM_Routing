import math
from typing import List, Tuple

# Sample output from the hypothetical solution
solution_robots_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 0]
]
solution_costs = [50, 60, 40, 55, 65, 70, 45, 85]

# City Coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(c1: Tuple[int, int], c2: Tuple[int, int]) -> float:
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def test_solution(tours: List[List[int]], costs: List[int]) -> str:
    # Test for the correct number of cities
    if len(cities_coordinates) != 23:
        return "FAIL"

    visited_cities = set()
    total_calculated_cost = 0

    for idx, tour in enumerate(tours):
        # Each tour must start and end at the depot city (0)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Visit each city and calculate travel cost
        calculated_cost = 0
        for i in range(len(tour)-1):
            city1, city2 = tour[i], tour[i+1]
            visited_cities.add(city1)
            if city1 != 0 or city2 != 0: # excluding depot to depot travel
                calculated_cost += euclidean_distance(cities_coordinates[city1], cities_coordinates[city2])
        
        # Check for match in reported and calculated travel costs
        if abs(calculated_cost - costs[idx]) > 0.1: # allow some floating-point differences
            return "FAIL"
        total_calculated_format += calculated_cost
    
    # Ensure all cities except the depot have been visited exactly once
    if len(visited_cities - {0}) != 22:
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Verify the solution provided
result = test_solution(solution_robots_tours, solution_costs)
print(result)