import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(tour, cities):
    # Requirement 1: Check if the path starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city."
    
    # Requirement 2: Check if each city is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return False, "Each city is not visited exactly once."
    
    # Requirement 5: Validate if output tour conforms to expected indices for cities
    if not all(isinstance(city, int) and 0 <= city < len(cities) for city in tour):
        return False, "Tour indices are not valid."

    return True, "Validations passed."

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def test_tour_and_cost():
    cities = [
        (53, 68), (75, 11), (91, 95), (22, 80),
        (18, 63), (54, 91), (70, 14), (97, 44),
        (17, 69), (95, 89)
    ]
    proposed_tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
    reported_cost = 290.8376577906224

    # Perform validation checks
    validation, message = validate_tour(proposed_tour, cities)
    if not validation:
        return "FAIL", message

    # Requirement 6: Check if the recalculated total travel cost matches the given one
    calculated_cost = calculate_total_travel_cancelled(proposed_tour, cities)
    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL", "Calculation mismatch in total travel cost."

    # All requirements satisfied
    return "CORRECT", "All requirements are satisfied."

# Execute the test case
result, reason = test_tour_and_cost()
print(result)  # Expected to print "CORRECT"
if result == "FAIL":
    print(reason)