import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def unit_test_tsp_solution(tour_solution, total_cost_solution, max_distance_solution):
    cities = [
        (8, 11),  # Depot City 0
        (40, 6),  # City 1
        (95, 33),  # City 2
        (80, 60),  # City 3
        (25, 18),  # City 4
        (67, 23),  # City 5
        (97, 32),  # City 6
        (25, 71),  # City 7
        (61, 16),  # City 8
        (27, 91),  # City 9
        (91, 46),  # City 10
        (40, 87),  # City 11
        (20, 97),  # City 12
        (61, 25),  # City 13
        (5, 59),  # City 14
        (62, 88),  # City 15
        (13, 43),  # City 16
        (61, 28),  # City 17
        (60, 63),  # City 18
        (93, 15)   # City 19
    ]

    # [Requirement 1] Check if each city is visited exactly once and starts/ends at the depot
    if tour_solution[0] != 0 or tour_solution[-1] != 0:
        return "FAIL"
    if sorted(tour_solution) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate actual total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour_solution) - 1):
        dist = euclidean_distance(cities[tour_solution[i]], cities[tour_solution[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # [Requirement 2] Maximize the longest distance between any two consecutive cities not tested as it's unclear the optimal.
    
    # [Requirement 3] Check the output
    if not math.isclose(total_cost, total_cost_solution, rel_tol=1e-9):
        return "FAIL"
    if not math.isclose(max_distance, max_distance_solution, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.1974047195548
max_distance = 32.38826948140329

# Test the solution
result = unit_test_tsp_solution(tour, total_cost, max_distance)
print(result)