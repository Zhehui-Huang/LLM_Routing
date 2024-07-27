import math
from itertools import chain

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, cities):
    depot_city = 0
    all_visited_cities = set()

    overall_cost = 0
    all_tours_start_and_end_at_depot = True
    all_cities_covered_exactly_once = True

    for robot_tour in tours:
        # Check starting and ending at depot
        if robot_tour[0] != depot_city or robot_tour[-1] != depot_city:
            all_tours_start_and_end_at_depot = False

        for i in range(len(robot_tour) - 1):
            overall_cost += euclidean_distance(cities[robot_tour[i]], cities[robot_tour[i+1]])

        # Collect visited cities excluding the depot for the cities visited exactly once condition
        visited_cities = set(robot_tour[1:-1])  # exclude first and last (depot occurrences)
        if len(visited_cities) != len(robot_tour[1:-1]):
            all_cities_covered_exactly_once = False
        all_visited_cities.update(visited_cities)

    # Check if all cities except depot are visited exactly once
    required_cities = set(range(1, len(cities)))  # all cities except the depot
    if all_visited_cities != required_cities:
        all_cities_covered_exactly_once = False
    
    return (all_tours_start_and_end_at_depot and
            all_cities_covered_exactly_once and
            # Returns "CORRECT" or "FAIL"
            "CORRECT" if all_tours_start_and_end_at_depot and all_cities_covered_exactly_once else "FAIL", 
            overall_cost)

# Define cities' coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Example solution (this should be replaced by actual solution output)
example_tours = [
    [0, 1, 2, 6, 5, 17, 22, 14, 0],
    [0, 7, 9, 13, 8, 3, 18, 19, 12, 11, 4, 15, 10, 0],
    [0, 16, 20, 21, 0]
]

verification_status, total_cost = verify_solution(example_tours, cities_coordinates)
print(verification_result)
print(f"Overall Total Travel Cost: {total_cost}")