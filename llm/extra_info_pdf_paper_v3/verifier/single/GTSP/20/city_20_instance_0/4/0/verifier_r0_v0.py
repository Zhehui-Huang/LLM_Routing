import math

# Define cities and groups
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Solution provided
tour = [0, 1, 8, 4, 0]
total_cost_provided = 110.09

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost_provided):
    # Test start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test visit exactly one city from each group
    visited_groups = set()
    for city_index in tour[1:-1]:  # Exclude the depot city at start and end
        for group_index, group_cities in groups.items():
            if city_index in group_cities:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Test total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost_provided, rel_tol=1e-2):
        return "FAIL"

    # Test output format (implicitly correct if past tests pass)
    return "CORRECT"

# Run the test
result = test_solution(tour, total_cost_provided)
print(result)