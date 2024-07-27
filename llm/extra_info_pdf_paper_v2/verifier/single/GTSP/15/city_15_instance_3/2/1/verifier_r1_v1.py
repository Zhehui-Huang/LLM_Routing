import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost_claimed):
    # Define coordinates for the cities including depot
    coordinates = [
        (16, 90),  # Depot city 0
        (43, 99),  # City 1
        (80, 21),  # City 2
        (86, 92),  # City 3
        (54, 93),  # City 4
        (34, 73),  # City 5
        (6, 61),   # City 6
        (86, 69),  # City 7
        (30, 50),  # City 8
        (35, 73),  # City 9
        (42, 64),  # City 10
        (64, 30),  # City 11
        (70, 95),  # City 12
        (29, 64),  # City 13
        (32, 79)   # City 14
    ]

    # Define groups of cities grouped by indices
    city_groups = [
        [1, 6, 14],
        [5, 12, 13],
        [7, 10],
        [4, 11],
        [2, 8],
        [3, 9]
    ]

    # Check robot starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if one city from each group is visited
    visited_from_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # Skip the depot at start and end
        found = False
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_from_groups[i]:
                    return "FAIL"  # City from the same group visited more than once
                visited_from_groups[i] = True
                found = True
                break
        if not found:
            return "FAIL"  # City not in any group
    if not all(visited_from_groups):
        return "FAIL"  # Not all groups were visited

    # Calculate total travel cost and compare with claimed
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    # Ensure the computed and claimed costs match closely
    if not math.isclose(total_cost_calculated, total_cost_claimed, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the solution
tour = [0, 14, 5, 10, 11, 2, 3, 0]
total_cost_claimed = 237.91874666073628
result = verify_solution(tour, total_cost_claimed)
print(result)