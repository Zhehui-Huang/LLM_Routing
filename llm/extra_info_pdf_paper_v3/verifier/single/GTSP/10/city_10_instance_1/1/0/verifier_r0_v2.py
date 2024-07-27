import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Coordinates for the cities
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    # Groups of cities
    groups = {
        0: set([5, 6, 7]),
        1: set([2, 3]),
        2: set([1, 9]),
        3: set([4, 8])
    }

    # [Requirement 1] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if there's exactly one city from each group visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot cities at the first and last positions
        for group_id, cities_in_group in groups.items():
            if city in cities_in_group:
                visited_groups.add(group_id)
    if len(visited_groups) != len(groups):
        return "FAIL"

    # [Requirement 3] & [Requirement 5] Calculate travel cost and compare with the provided total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 5, 2, 9, 8, 0]
total_cost = 183.99

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)