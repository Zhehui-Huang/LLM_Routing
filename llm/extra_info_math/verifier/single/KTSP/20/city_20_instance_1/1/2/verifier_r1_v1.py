import math

# Define the given cities based on their coordinates
cities = {
    0: (14, 77),
    6: (4, 56),
    2: (19, 38),
    13: (26, 29),
    8: (37, 28),
    9: (27, 45),
    14: (21, 79)
}

# Provided solution for comparison
solution_tour = [0, 6, 2, 13, 8, 9, 14, 0]
provided_travel_cost = 130.6658168109853

def calculate_euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities with their coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_tour(tour, expected_length):
    """Verify the tour starts and ends at the depot (0), and has exactly `expected_length` different cities."""
    return tour[0] == 0 and tour[-1] == 0 and len(set(tour)) == expected_length

def calculate_total_travel_cost(tour):
    """Calculate the total travel cost of the tour based on Euclidean distance."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution():
    # Check Requirement 1 and 2
    if not verify_tour(solution_tour, 7):
        return "FAIL"

    # Calculate the real travel cost
    actual_travel_cost = calculate_total_travel_cost(solution_tour)
    
    # Check Requirement 3: Comparison of expected and calculated travel cost
    if not math.isclose(actual_travel_cost, provided_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the unit tests to verify the solution
print(test_solution())