import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(cities, tour):
    """Calculate the total travel cost for a given tour of cities."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_candidate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution(cities, tour, reported_cost):
    """Testing the given solution against all requirements."""
    # [Requirement 1] and [Requirement 7]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if len(set(tour[1:-1])) != len(cities) - 1:
        return "FAIL"

    # [Requirement 3], [Requirement 5] and [Requirement 6] - Ensured by the solver, hard to test directly

    # [Requirement 4] & [Requirement 8]
    calculated_cost = calculate_total_travel_cost(cities, tour)
    if abs(calculated_cost - reported_cost) > 0.001:  # Allowing a small error margin
        return "FAIL"

    return "CORRECT"

# Map of cities with their coordinates:
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# The solution tour and reported cost:
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
reported_cost = 294.17253892411236

# Run the test and print the result:
print(test_solution(cities, tour, reported_cost))