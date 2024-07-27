import math
from itertools import chain

# Define the coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot tours provided
tours = [
    [0, 4, 15, 0],
    [0, 20, 12, 0],
    [0, 7, 21, 0],
    [0, 14, 19, 0],
    [0, 8, 22, 0],
    [0, 13, 5, 0],
    [0, 16, 11, 0],
    [0, 18, 6, 0]
]

# Corresponding tour costs provided
provided_costs = [
    61.07512778319072, 77.84047551214809, 44.358534765286805,
    117.09903531895705, 79.64626217740934, 68.36272673975597,
    62.757003433155134, 81.18185306390538
]

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def verify_tours(tours, cities, provided_costs):
    visited = set()
    total_calculated_cost = 0.0
    
    for tour, provided_cost in zip(tours, provided_costs):
        start_depot = tour[0]
        if start_depot != 0:
            return "FAIL: Not all robots start at Depot city 0"
        
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            tour_cost += euclidean_distance(cities[city_from], cities[city_to])
            visited.add(city_from)
        
        if abs(tour_cost - provided_cost) > 0.001:  # Allowing a small margin for floating-point comparison
            return "FAIL: Incorrect tour cost calculation"

        total_calculated_cost += tour_cost
        
    if visited != set(cities.keys()):
        return "FAIL: Not all cities are visited exactly once"

    if abs(total_calculated_cost - sum(provided_costs)) > 0.001:
        return "FAIL: Incorrect total travel cost calculation"
    
    return "CORRECT"

# Execute the test
result = verify_tours(tours, cities, provided_costs)
print(result)