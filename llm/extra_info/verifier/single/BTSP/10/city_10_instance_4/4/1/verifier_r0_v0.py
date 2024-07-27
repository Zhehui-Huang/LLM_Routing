import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tour, total_cost, max_distance):
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
    
    # Verify number of cities
    if len(coordinates) != 10:
        return "FAIL"
    
    # Verify start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the robot visits each city exactly once (excluding depot occurring twice)
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Calculate total travel cost and max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
    
    # Verify the total cost is correct
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Verify the maximum distance between consecutive cities
    if not (math.isinf(max_distance) or math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Proposed solution information
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_travel_cost = 637.82
maximum_distance = float('inf')  # As the solution suggests "inf" as the max distance

# Verify the solution
result = verify_solution(tour, total_travel_id_cost, maximum_distance)
print(result)