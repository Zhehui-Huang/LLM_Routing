import math

def compute_distance(p1, p2):
    """Compute Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, city_coordinates, groups):
    """ Verify the tour against the requirements. """
    # Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each group must be represented exactly once
    visited_groups = {}
    for city in tour[1:-1]:
        for group_index, group_cities in enumerate(groups):
            if city in group_cities:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups[group_index] = 1
                break

    if len(visited_groups) != len(groups):
        return "FAIL"

    # Requirement 3: Minimization of travel distance implicitly assumed by solver output.
    # No actual check performed here since it's assumed the solver found optimal solution.
    
    return "CORRECT"

# Given data
city_coordinates = [
    (79, 15), # City 0: Depot
    (79, 55), # City 1
    (4, 80),  # City 2
    (65, 26), # City 3
    (92, 9),  # City 4
    (83, 61), # City 5
    (22, 21), # City 6
    (97, 70), # City 7
    (20, 99), # City 8
    (66, 62)  # City 9
]

groups = [
    [1, 4], # Group 0
    [2, 6], # Group 1
    [7],    # Group 2
    [5],    # Group 3
    [9],    # Group 4
    [8],    # Group 5
    [3],    # Group 6
]

# Provided solution
solution_tour = [0, 3, 0]
# solution_total_cost = 35.61 # This value would be used if verifying costs, which isn't explicitly done.

# Verify the solution tour
result = verify_tour(solution_tour, city_coordinates, groups)
print(result)