import math

# City coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

def euclidean_distance(A, B):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

def check_solution(tour, total_cost, max_distance):
    # Handle case where no valid tour is found
    if len(tour) == 0:
        if total_cost == 0 and max_distance == 0:
            return "CORRECT"
        else:
            return "FAIL"

    # [Requirement 1] Tour starts and ends at the depot city
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # [Requirement 2] Ensuring all cities are visited exactly once, and tour length checks
    if len(set(tour)) != 21 or len(tour) != 21:
        return "FAIL"
    
    calculated_cost = 0
    calculated_max_dist = 0
    
    # Calculate distances and check [Requirement 3, 6, 7]
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist
            
    # Validate total travel cost and maximum distance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    if not math.isclose(calculated_max_dist, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# No valid tour found scenario
tour_result = []  # No tour
total_cost_result = 0  # Should be 0 as no travel occurs
max_distance_result = 0  # Should be 0 as no distances are covered

# Run the adjusted test
print(check_solution(tour_result, total_cost_result, max_distance_result))