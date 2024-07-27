import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, city_groups, expected_cost):
    # Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:
        for idx, group in enumerate(city_json):
            if city in group:
                visited_groups.append(idx)
    if sorted(set(visited_json)) != sorted([0, 1, 2]):
        return "FAIL"

    # Calculate the travel cost and compare with expected
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (8, 11),   # 0
    (40, 6),   # 1
    (95, 33),  # 2
    (80, 60),  # 3
    (25, 18),  # 4
    (67, 23),  # 5
    (97, 32),  # 6
    (25, 71),  # 7
    (61, 16),  # 8
    (27, 91),  # 9
    (91, 46),  # 10
    (40, 87),  # 11
    (20, 97),  # 12
    (61, 25),  # 13
    (5, 59),   # 14
    (62, 88),  # 15
    (13, 43),  # 16
    (61, 28),  # 17
    (60, 63),  # 18
    (93, 15)   # 19
]

# City groups
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Test solution
tour = [0, 1, 8, 4, 0]
expected_cost = 110.088

# Verify
result = verify_solution(tour, cities, city_groups, expected_cost)
print(result)