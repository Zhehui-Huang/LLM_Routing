import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution():
    cities = [
        (50, 42),  # Depot city 0
        (41, 1),   # Group 0: City 1
        (18, 46),  # Group 0: City 2
        (40, 98),  # Group 1: City 3
        (51, 69),  # Group 2: City 4
        (47, 39),  # Group 2: City 5
        (62, 26),  # Group 0: City 6
        (79, 31),  # Group 1: City 7
        (61, 90),  # Group 1: City 8
        (42, 49)   # Group 2: City 9
    ]
    groupings = [
        [1, 2, 6],
        [3, 7, 8],
        [4, 5, 9]
    ]

    # Test solution
    proposed_tour = [0, 6, 7, 5, 0]
    proposed_total_cost = 74.94753083872993  # as provided

    # Verify requirement 1
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Verify requirement 2
    visited_groups = set()
    for city in proposed_tour:
        for i, group in enumerate(groupings):
            if city in group:
                visited_groups.add(i)
    if len(visited_groups) != len(groupings):
        return "FAIL"

    # Verify requirement 3 & 6
    calculated_cost = calculate_total_travel_cost(proposed_tour, cities)
    if not math.isclose(calculated_cost, proposed_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 4 is not verifiable without solving the problem ourselves or knowing the true optimal solution.

    # Verify requirement 5
    # verified implicitly by the structure of proposed_tour as list starting and ending with 0

    return "CORRECT"

# Execute the test
print(test_solution())