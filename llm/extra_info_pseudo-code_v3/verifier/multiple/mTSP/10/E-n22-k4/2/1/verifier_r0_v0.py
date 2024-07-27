import numpy as np
import math

# Distances are provided from the solution using the Euclidean distance formula
ROBOTS_TOURS = [
    [0, np.int64(14), np.int64(16), np.int64(12), np.int64(15), np.int64(18), 0],
    [0, np.int64(10), np.int64(8), np.int64(6), np.int64(3), np.int64(4), np.int64(11), 0],
    [0, np.int64(13), np.int64(19), np.int64(21), np.int64(17), np.int64(20), 0],
    [0, np.int64(9), np.int64(7), np.int64(5), np.int64(2), np.int64(1), 0]
]

ROBOTS_TOUR_COSTS = [87.16778614302781, 99.60668471182551, 109.77573076701911, 111.83855721201843]
OVERALL_COST = 408.38875883389085

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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

def test_solution():
    visited_cities = set()

    # Test each robot's tour
    for robot_id, tour in enumerate(ROBOTS_TOURS):
        # Check start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL")
            return

        # Check cities are only visited once and calculate cost
        total_calculated_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            visited_cities.add(city1)
            total_calculated_cost += calculate_distance(CITIES[city1], CITIES[city2])

        # Compare calculated cost to reported cost
        if not np.isclose(total_calculated_cost, ROBATRIX_TOUR_COSTS[robot_id], atol=1e-5):
            print("FAIL")
            return

    # Check if exactly all cities are visited except the depot (0)
    if len(visited_cities) != len(CITIES) or 0 in visited_cities:
        print("FAIL")
        return

    # Check overall cost
    if not np.isclose(sum(ROBOTS_TOUR_COSTs), OVERALL_COST, atol=1e-5):
        print("FAIL")
        return

    print("CORRECT")

test_solution()