import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour(tour, cities):
    # Requirement 1: Start and end at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at depot city."

    # Requirement 2: Visit all other cities exactly once
    visited = set(tour)
    if len(tour) != len(cities) or len(visited) != len(cities):
        return False, "Tour does not visit all cities exactly once."

    return True, "Tour validation successful."

def calculate_total_travel_cost(tour, cities):
    total_cost = 0.0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

def test_solution(tour, total_cost, cities):
    # Validate the tour
    validity, message = validate_tour(tour, cities)
    if not validity:
        return "FAIL", message

    # Requirement 3: Check if the total travel cost is calculated correctly
    calculated_cost = calculate_total_travel_cost(tour, cities)
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-3):
        return "FAIL", f"Reported total travel cost is not correct. Expected: {calculated_cost}, Got: {total_cost}"
    
    # If all checks passed
    return "CORRECT", "All requirements satisfied."

# City coordinates 
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Provided solution
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_cost_reported = 322.50

# Run test
status, message = test_solution(tour, total_cost_reported, cities)
print(status)