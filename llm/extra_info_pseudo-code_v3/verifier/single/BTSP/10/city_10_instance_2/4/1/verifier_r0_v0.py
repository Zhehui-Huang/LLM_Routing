import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, cities):
    # Check if the tour starts and ends at the city 0 (depot)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at depot city."
    # Check if all cities are visited exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return False, "Each city is not visited exactly once."
    return True, ""

def calculate_total_and_max_distance(tour, cities):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

def test_solution():
    # Coordinates of the cities (depot + cities 1 through 9)
    cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), 
              (23, 95), (20, 56), (49, 29), (13, 17)]
    # Presumed solution from the example
    provided_tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
    provided_total_cost = 418.32344417340323
    provided_max_distance = 69.42621983083913
    
    # Verify requirements for the tour
    valid, message = verify_tour(provided_tour, cities)
    if not valid:
        return "FAIL", message

    # Calculate distances
    calculated_total_cost, calculated_max_distance = calculate_total_and_max_distance(provided_tour, cities)
    
    # Check calculated values against provided solution
    if not math.isclose(provided_total_cost, calculated_total_cost, rel_tol=1e-6):
        return "FAIL", "Total travel cost mismatch."
    if not math.isclose(provided_max_distance, calculated_max_distance, rel_tol=1e-6):
        return "FAIL", "Maximum distance mismatch."

    # All checks passed
    return "CORRECT", ""

# Call the test function
result, reason = test_solution()
if result == "CORRECT":
    print("CORRECT")
else:
    print(f"FAIL: {reason}")