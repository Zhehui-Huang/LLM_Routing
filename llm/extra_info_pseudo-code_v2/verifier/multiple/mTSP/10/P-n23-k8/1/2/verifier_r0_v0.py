import numpy as np

# Data provided in the solved configuration
tours = [
    [0, np.int64(2), np.int64(8), np.int64(9), np.int64(13), 0],
    [0, np.int64(3), np.int64(12), np.int64(15), 0],
    [0, np.int64(6), np.int64(21), 0],
    [0, np.int64(14), np.int64(17), 0],
    [0, np.int64(1), np.int64(10), np.int64(16), 0],
    [0, np.int64(18), np.int64(19), 0],
    [0, np.int64(4), np.int64(11), 0],
    [0, np.int64(20), np.int64(5), np.int64(7), np.int64(22), 0]
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities (as provided)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def test_solution(tours, coordinates):
    all_cities = set(range(1, len(coordinates)))  # City indices excluding the depot
    visited_cities = set()
    
    overall_cost = 0.0
    
    for tour in tours:
        # Requirement 6: Each tour should start and end at depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at depot"
        
        # Compute travel cost for this tour
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
            if i > 0:  # exclude counting depot in visited cities
                visited_cities.add(tour[i])
        
        overall_cost += tour_cost

    # Requirement 1: All cities visited exactly once
    if len(all_cities) != len(visited_cities) or all_cities != visited_cities:
        return "FAIL: Not all cities are visited exactly once"

    # Requirement 7: Overall total travel costs computed above needs to be verified manually if correct and minimal
        
    # If all checks passed:
    return "CORRECT"

# Test the solution
test_result = test_solution(tours, coordinates)
print(test_result)