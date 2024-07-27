import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour(tour, groups, cities, depot_index, expected_cost):
    # Requirement 1: Check start and end at depot city.
    if tour[0] != depot_index or tour[-1] != depot_index:
        return "FAIL"
    
    # Requirement 2: Check each group is represented exactly once by one city in the tour.
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(groups):
            if city in group and group_index not in visited_groups:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Requirement 3: Calculate and verify the travel cost.
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_distance, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks are passed:
    return "CORRECT"

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Group information
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

# Tour information
tour = [0, 14, 5, 10, 11, 8, 9, 0]
expected_cost = 166.75801920718544

# Check the solution
result = test_tour(tour, groups, cities, 0, expected_cost)
print(result)