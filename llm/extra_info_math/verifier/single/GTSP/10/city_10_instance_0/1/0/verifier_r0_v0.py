import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates, groups):
    # [Requirement 1] Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if the robot visits exactly one city from each of the three city groups
    visited_cities = tour[1:-1]  # remove the starting and ending depot entries
    unique_group_visit = set()
    for city in visited_cities:
        for idx, group in enumerate(groups):
            if city in group:
                unique_group

_visit.add(idx)
                break
    if len(unique_group_visit) != 3:
        return "FAIL"
    
    # Calculate travel distance and compare with total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # [Requirement 3] Check if the given total_cost matches the calculated cost based on Euclidean distances
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates (0 is the depot)
city_coordinates = [
    (50, 42),  # Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Define groups
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Given solution from the solver
tour = [0, 5, 0]
total_travel_cost = 8.48528137423857

# Perform the verification
verification_result = verify_solution(tour, total_travel_test, city_coordinates, groups)
print(verification_result)