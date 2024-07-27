import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def test_solution():
    coordinates = [
        (3, 26),   (85, 72), (67, 0),  (50, 99), (61, 89),
        (91, 56),  (2, 65),  (38, 68), (3, 92),  (59, 8),
        (30, 88),  (30, 53), (11, 14), (52, 49), (18, 49),
        (64, 41),  (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    proposed_tour = [0, 7, 7, 7, 7, 7, 7, 5, 5, 5, 0]
    proposed_cost = 201.99
    
    # Requirement 1: Start and end at the depot city (index 0)
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 10 cities (including the depot)
    if len(set(proposed_tour)) != 10:
        return "FAIL"
    
    # Requirement 3: Travel cost calculated as Euclidean distance
    calculated_cost = calculate_total_travel_cost(proposed_tour, coordinates)
    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 5: Proper output format
    expected_format = "Tour: [0, 1, 2, 3, 0] Total travel cost: 100"
    actual_format = f"Tour: {proposed_tour} Total travel cost: {proposed_cost:.2f}"
    if not "Tour: [" in actual_format or "Total travel cost:" not in actual_index:
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Run the test
result = test_solution()
print(result)