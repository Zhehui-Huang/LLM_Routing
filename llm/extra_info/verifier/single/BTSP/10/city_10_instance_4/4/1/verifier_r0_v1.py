import math

def euclidean_distance(coord1, coord2):
    """Calculates the Euclidean distance between two city coordinates."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    """Verifies the solution against the specified requirements."""
    # City coordinates
    coordinates = [
        (79, 15),  # Depot city
        (79, 55),
        (4, 80),
        (65, 26),
        (92, 9),
        (83, 61),
        (22, 21),
        (97, 70),
        (20, 99),
        (66, 62)
    ]
    
    # Requirement checks
    if len(coordinates) != 10:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Calculate total travel cost and max distance verification
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    if max_distance != float('inf') and not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_travel_cost = 637.82
maximum_distance = float('inf')  # As provided in the problem description

# Running verification
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)