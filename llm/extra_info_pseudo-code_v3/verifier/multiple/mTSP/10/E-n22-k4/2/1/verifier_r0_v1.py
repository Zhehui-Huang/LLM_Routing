import numpy as np
import math

# Provided tours and costs for Robots
ROBOTS_TOURS = [
    [0, 14, 16, 12, 15, 18, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 13, 19, 21, 17, 20, 0],
    [0, 9, 7, 5, 2, 1, 0]
]

ROBOTS_TOUR_COSTS = [87.16778614302781, 99.60668471182551, 109.77573076701911, 111.83855721201843]
OVERALL_COST = 408.38875883389085

# Cities and their coordinates
CITIES = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

def calculate_distance(city1, city2):
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    visited_cities = set()

    for robot_id, tour in enumerate(ROBOTS_TOURS):
        # Check start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return

        # Check cities are visited once and compute cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            visited_cities.add(city1)
            calculated_cost += calculate_distance(city1, city2)

        # Check cost consistency
        if not np.isclose(calculated_cost, ROBOTS_TOUR_COSTS[robot_id], atol=1e-5):
            print("FAIL")
            return

    # Verify all cities except depot are visited exactly once
    if visited_cities != set(range(1, 22)):
        print("FAIL")
        return

    # Verify overall cost
    if not np.isclose(sum(ROBOTS_TOUR_COSTS), OVERALL_COST, atol=1e-5):
        print("FAIL")
        return

    print("CORRECT")

test_solution()