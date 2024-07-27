def verify_solution(tour, total_cost, max_distance, coordinates):
    # Requirement 1: Tour must start and end at the depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once
    unique_cities = set(tour[1:-1])  # exclude depot city at start and end
    if len(unique_cities) != len(coordinates) - 1:
        return "FAIL"
    
    # Calculate the actual travel cost and maximum distance between consecutive cities
    import math
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check total travel cost
    if not math.isclose(calculated_cost, total, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 3: Check if the maximum distance is minimized (or reasonable)
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given solution values
tour = [0, 4, 8, 3, 5, 9, 2, 7, 1, 6, 0]
total = 289.0753138987659
max_dist = 56.61271941887264
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91),
               (70, 14), (97, 44), (17, 69), (95, 89)]

# Verify the solution
print(verify_solution(tour, total, max_dist, coordinates))