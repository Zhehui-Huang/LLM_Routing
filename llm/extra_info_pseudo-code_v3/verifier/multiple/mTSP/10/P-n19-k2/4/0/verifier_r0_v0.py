import math

# City coordinates as per the problem statement, indexed by city number
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Tours and their expected travel costs as provided
tours = [
    ([0, 1, 10, 4, 11, 14, 12, 3, 17, 16, 0], 123.69),
    ([0, 8, 2, 7, 9, 15, 13, 5, 18, 6, 0], 113.38)
]

def verify_tours(tours):
    visited_cities = set()
    total_cost_calculated = 0.0

    for tour, expected_cost in tours:
        # Check if all segments start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour does not start and end at the depot.")
            return "FAIL"

        tour_cost = 0.0
        for i in range(len(tour) - 1):
            cd = euclidean_distance(tour[i], tour[i + 1])
            tour_cost += cd
            visited_cities.add(tour[i])

        if abs(tour_cost - expected_cost) > 1e-2:
            print(f"FAIL: Calculated cost {tour_cost} does not match expected cost {expected_cost}.")
            return "FAIL"
        
        total_cost_calculated += tour_cost

    # Check if all cities except the depot are visited exactly once
    if len(visited_cities) != len(cities) - 1:
        print("FAIL: Not all cities were visited exactly once, or a city was visited more than once.")
        return "FAIL"

    # Overall total travel cost (expected is directly added from individual costs above)
    if abs(total_cost_calculated - 237.08) > 1e-2:
        print(f"FAIL: Total calculated travel cost {total_cost_calculated} does not match expected total.")
        return "FAIL"

    return "CORRECT"

# Unit Test Execution
result = verify_tours(tours)
print(result)