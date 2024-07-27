import math
from typing import List, Tuple

# Define city coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Mocked output from solution with algorithms details omitted for brevity
robots_tours = [
    [0, 8, 3, 0],
    [1, 10, 15, 1],
    [2, 18, 19, 2],
    [3, 12, 11, 3],
    [4, 16, 4],
    [5, 14, 17, 5],
    [6, 20, 22, 9, 6],
    [7, 21, 13, 7]
]

# Check if solution is correct
def check_solution(tours: List[List[int]], coordinates: List[Tuple[int, int]]):
    visited_cities = set()
    total_travel_cost = 0

    def euclidean_distance(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
    
    for tour in tours:
        for i in range(len(tour) - 1):
            city_current, city_next = tour[i], tour[i+1]
            total_travel_cost += euclidean_distance(coordinates[city_current], coordinates[city_next])
            visited_cities.add(city_current)
        # Check if tour ends at the start depot
        if tour[0] != tour[-1]:
            return "FAIL"
    
    # Check if all cities are visited exactly once
    if len(visited_cities) != len(coordinates):
        return "FAIL"
    
    # Requirements met
    return total_travel_cost

# Perform the verification
result = check_solution(robots_tours, cities_coordinates)
expected_cities_count = len(cities_coordinates)
visited_cities_count = len(set(sum(robots_tours, [])))

# Check if requirements are met
if isinstance(result, float) and visited_cities, count == expected_cities_count:
    print("CORRECT")
else:
    print("FAIL")