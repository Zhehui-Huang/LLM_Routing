import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, coordinates):
    # Check if the robot starts and ends its journey at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city."
    
    # Check if each city is visited exactly once (except the depot city which should be visited twice)
    if set(tour) != set(range(len(coordinates))):
        return False, "Tour does not visit each city exactly once."
    
    # Total travel cost calculation
    total_cost = sum(calculate_distance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                        coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
                     for i in range(len(tour)-1))
    
    # Calculation for the maximum distance between any two consecutive cities in the tour
    max_distance = max(calculate_rpundtance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                            coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
                       for i in range(len(tour)-1))
    
    return True, total_cost, max_distance

def test_solution():
    coordinates = [
        (54, 87), # Depot 0
        (21, 84),
        (69, 84),
        (53, 40),
        (54, 42),
        (36, 30),
        (52, 82),
        (93, 44),
        (21, 78),
        (68, 14),
        (51, 28),
        (44, 79),
        (56, 58),
        (72, 43),
        (6, 99)  # City 14
    ]
    
    solution_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
    provided_total_cost = 676.812946106938
    provided_max_distance = 0
    
    valid, calculated_cost, calculated_max_distance = validate_tour(solution_tour, coordinates)
    if not valid:
        return "FAIL due to invalid tour:", calculated_cost
    
    if abs(provided_total_cost - calculated_cost) > 1e-6 or abs(provided_max_distance - calculated_max_distance) > 1e-6:
        return "FAIL due to incorrect cost/distances"
    
    return "CORRECT"

# Execute the test
test_result = test_solution()
print(test_result)