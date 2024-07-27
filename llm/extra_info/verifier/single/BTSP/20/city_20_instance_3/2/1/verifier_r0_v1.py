import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_cost, max_distance):
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
        (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
        (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Check if starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start or end at the depot."
    
    # Check if all cities are visited exactly once
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):
        return "FAIL: Not all cities are visited exactly once."
    
    # Calculate the travel cost and max distance
    computed_cost = 0
    computed_max_distance = float('-inf')
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        computed_cost += dist
        computed_max_distance = max(computed_max_distance, dist)
    
    # Check total cost and max distance calculations
    if not math.isclose(computed_cost, total_cost, abs_tol=1e-2):
        return f"FAIL: Computed cost ({computed_cost:.2f}) does not match given total cost ({total_cost:.2f})."

    if not math.isclose(computed_max_distance, max_distance, abs_tol=1e-2):
        return f"FAIL: Computed max distance ({computed_max_distance:.2f}) does not match given max distance ({max_distance:.2f})."

    # If all checks are correct
    return "CORRECT"

# Input values
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.37
max_consecutive_distance = 68.15

# Run the test
result = test_solution(tour, total_travel_cost, max_consecutive_distance)
print(result)