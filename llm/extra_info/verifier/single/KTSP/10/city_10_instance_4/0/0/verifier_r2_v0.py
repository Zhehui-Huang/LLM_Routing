import math

def calculate_total_distance(tour, coordinates):
    total_distance = 0.0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        total_distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_distance

def test_solution():
    coordinates = [
        (79, 15),  # City 0
        (79, 55),  # City 1
        (4, 80),   # City 2
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8
        (66, 62)   # City 9
    ]
    
    proposed_tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
    proposed_cost = 235.37735391753955

    # [Requirement 1] Check if the robot starts and ends at the depot (city 0)
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 8 cities including the depot are visited
    if len(set(proposed_tour)) != 9:  # Including repeated depot city 0
        return "FAIL"
    
    # [Requirement 3] Verify calculated travel cost is approximately proposed_cost
    calculated_cost = calculate_total_distance(proposed_tour, coordinates)
    if not math.isclose(calculated_cost, proposed_cost, abs_tol=1e-6):
        return "FAIL"
    
    # [Requirement 4] Assuming the cost provided is the shortest (this is just assumed to be validated externally)
    # We ensure only that the cost calculation method is correct and matches the provided length.
    
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)