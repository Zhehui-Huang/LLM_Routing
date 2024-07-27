import math
from typing import List, Tuple

# Define helper function to compute Euclidean distance
def calculate_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Test function to verify the TSP solution
def verify_tsp_solution(tours: List[List[int]], costs: List[float], cities: List[Tuple[int, int]]):
    expected_total_cost = 185.24224625522046  # Overall expected total cost from solution
    
    # Check if tours start and end at their assigned depots, and calculate travel costs
    calculated_costs = []
    visited_cities = set()
    for i, tour in enumerate(tours):
        if tour[0] != tour[-1] or tour[0] != i:  # first element should be the same as the last and should match the robot's depot id
            print("Tour does not start and end at the correct depot for robot", i)
            return "FAIL"
        
        tour_cost = 0
        for j in range(1, len(tour)):
            tour_cost += calculate_distance(cities[tour[j-1]], cities[tour[j]])
            visited_cities.add(tour[j-1])
            visited_cities.add(tour[j])

        calculated_costs.append(tour_cost)
        if not math.isclose(tour_cost, costs[i], abs_tol=0.001):
            print(f"Cost mismatch for robot {i}. Calculated cost: {tour_cost}, Expected cost: {costs[i]}")
            return "FAIL"
    
    if len(visited_cities) != len(cities):
        print("Not all cities were visited exactly once.")
        return "FAIL"
    
    total_calculated_cost = sum(calculated_costs)
    if not math.isclose(total_calculated_cost, expected_total_cost, abs_tol=0.001):
        print(f"Total cost mismatch. Calculated total cost: {total_calculated_cost}, Expected total cost: {expected_total_cost}")
        return "FAIL"
    
    return "CORRECT"

# Test data
tours = [
    [0, 21, 0],
    [1, 10, 16, 1],
    [2, 13, 2],
    [3, 8, 18, 19, 12, 3],
    [4, 11, 15, 4],
    [5, 22, 17, 14, 5],
    [6, 20, 6],
    [7, 9, 7]
]

costs = [
    4.47213595499958,
    24.85853025288332,
    18.110770276274835,
    50.55066424081727,
    26.480522629341756,
    27.253463793663165,
    13.416407864998739,
    20.09975124224178
]

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

result = verify_tsp_solution(tours, costs, cities)
print(result)