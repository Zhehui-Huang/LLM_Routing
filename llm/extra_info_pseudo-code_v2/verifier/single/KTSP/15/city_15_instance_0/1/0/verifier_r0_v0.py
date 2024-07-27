import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def check_solution(tour, reported_cost):
    # City coordinates
    coordinates = [
        (9, 93),  # City 0
        (8, 51),  # City 1
        (74, 99), # City 2
        (78, 50), # City 3
        (21, 23), # City 4
        (88, 59), # City 5
        (79, 77), # City 6
        (63, 23), # City 7
        (19, 76), # City 8
        (21, 38), # City 9
        (19, 65), # City 10
        (11, 40), # City 11
        (3, 21),  # City 12
        (60, 55), # City 13
        (4, 39)   # City 14
    ]

    # Requirement 1: Tour starts and ends at depot city, City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The tour must exactly include 4 cities
    if len(tour) != 5:  # Includes the return to the depot
        return "FAIL"
    
    # Requirement 3: Validate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    # Requirement 4: Validate that path is feasible (all indices must be valid)
    if any(t not in range(len(coordinates)) for t in tour):
        return "FAIL"
    
    # All requirements met
    return "CORRECT"

# Tour and cost reported
tour = [0, 1, 10, 8, 0]
reported_cost = 90.54

# Run the unit test
result = check_solution(tour, reported_cost)
print(result)