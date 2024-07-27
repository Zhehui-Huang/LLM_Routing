import math
from collections import Counter

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour_distance(tour, coordinates):
    """Calculate the total travel cost of the tour"""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return round(total_cost, 2)

def verify_solution():
    # City coordinates
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
        18: (62, 63), 19: (63, 69), 20: (45, 35)
    }
    # City demands
    demands = {
        0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8,
        11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15
    }
    # Tours and reported costs
    tours = [
        ([0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0], 135.57),
        ([0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0], 160.83)
    ]
    robot_capacity = 160
    cities_visited = []

    # Check each tour
    for tour, reported_cost in tours:
        total_demand = sum(demands[city] for city in tour if city != 0)
        if total_demand > robot_capacity:
            return "FAIL"

        calculated_cost = check_tour_distance(tour, coordinates)
        if abs(calculated_cost - reported_cost) > 0.1:
            return "FAIL"

        cities_visited.extend(tour)

    # Check all cities visited exactly once and only once (except depot which is multiple times)
    city_count = Counter(cities_visited)
    del city_count[0]  # Remove depot check
    if not all(count == 1 for count in city_count.values()):
        return "FAIL"
    
    # Check if all cities are accounted for
    if len(city_count) != 21 - 1:  # excluding the depot
        return "FAIL"
    
    return "CORRECT"

# Running the verification function
result = verify_solution()
print(result)