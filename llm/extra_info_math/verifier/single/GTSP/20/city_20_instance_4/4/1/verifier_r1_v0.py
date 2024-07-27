import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

groups = {
    0: [5, 6, 16],
    1: [8, 18, 19],
    2: [11, 12, 13],
    3: [1, 3, 9],
    4: [2, 4, 14],
    5: [10, 17],
    6: [7, 15]
}

# Solution provided
tour = [0, 4, 0]
travel_cost = 104.4030650891055

def verify_requirements(tour, travel_cost, cities, groups):
    # Check requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Visit exactly one city from each group
    visited_cities = set(tour)
    if len(visited_cities) != len(groups) + 1:
        return "FAIL"
    for group in groups.values():
        if not visited_cities.intersection(set(group)):
            return "FAIL"

    # Check requirement 3: Shortest possible tour
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(computed_cost, travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Evaluate the correctness of the provided solution
result = verify_requirements(tour, travel_cost, cities, groups)
print(result)