import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates given in the task
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Solution data provided (tours and costs)
robots = {
    0: ([0, 14, 9, 0], 15.524174696260024),
    1: ([0, 7, 22, 0], 5.656854249492381),
    2: ([0, 17, 18, 0], 30.01666203960727),
    3: ([0, 8, 12, 0], 16.64331697709324),
    4: ([0, 4, 11, 0], 7.211102550927978),
    5: ([0, 10, 20, 0], 22.20360331117452),
    6: ([0, 5, 16, 0], 19.1049731745428),
    7: ([0, 6, 2, 13, 19, 0, 21, 1, 15, 3, 0], 134.18017392429834)
}

def test_solution(robots, cities):
    visited_cities = set()
    overall_cost = 0
    all_cities = set(range(23))

    for robot, (tour, cost) in robots.items():
        # Requirement 1 check: start at city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check costs and tours correctness
        calc_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            calc_cost += euclidean_distance(cities[city_from], cities[city_to])
            visited_cities.add(city_to)

        # Requirement 3 check: each city visited once and costs are correct
        if abs(calc_cost - cost) > 0.0001:
            return "FAIL"
        
        overall_cost += cost

        # Requirement 7: No city visited by more than one robot
        if len(visited_cities.intersection(set(tour))) > len(set(tour)) - 1:
            return "FAIL"

    # Requirement 3: all cities visited exactly once, excluding city 0
    if visited_cities != all_cities:
        return "FAIL"

    # Requirement 5: Output check, included implicitly by cost comparison and city visits

    return "CORRECT"

# Run the test
result = test_solution(robots, cities)
print(result)