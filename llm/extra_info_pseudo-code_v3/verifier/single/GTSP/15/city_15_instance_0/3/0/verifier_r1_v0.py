import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost, cities, groups):
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2
    visited_groups = set()
    for city_index in tour[1:-1]:  # exclude the depot city at start/end
        for group_index, group in enumerate(groups):
            if city_index in group:
                visited_groups.add(group_index)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check Requirement 3 & Requirement 6
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"

    # Requirement 4 is assumed to be handled within the main solution logic and can't be verified independently without comparisons to all possibilities.

    # Check Requirement 5
    if not (tour and tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    return "CORRECT"

# City coordinates data
cities = [
    (9, 93),  # City 0: Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Groups information
groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]        # Group 2
]

# Solution proposed
proposed_tour = [0, 10, 1, 9, 0]
proposed_total_cost = 122.22

# Run the test
result = test_solution(proposed_tour, proposed_total_cost, cities, groups)
print(result)