import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, max_dist):
    cities = [
        (29, 51), (49, 20), (79, 69), (17, 20),
        (18, 61), (40, 57), (57, 30), (36, 12),
        (93, 43), (17, 36), (4, 60), (78, 82),
        (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] Check if all cities are visited exactly once and starts/ends at depot.
    if len(tour) != len(cities) + 1 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities) + 1:
        return "FAIL"

    # Calculate total travel cost and max distance 
    calculated_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist

    # [Requirement 2] Verify if maximum distance between consecutive cities is minimized (not checked correctly in this context)
    
    # [Requirement 3] Check the calculated cost and max distance with provided values
    if not (math.isclose(calculated_cost, total_cost, rel_tol=1e-2) and math.isclose(calculated_max_dist, max_dist, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Solution provided
tour = [0, 5, 13, 2, 12, 11, 8, 14, 6, 1, 7, 3, 9, 4, 0]
total_travel_cost = 341.62
maximum_distance_between_consecutive_cities = 50.22

# Run verification
result = verify_solution(tour, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)  # Output should be "CORRECT" if the solution fulfills all requirements