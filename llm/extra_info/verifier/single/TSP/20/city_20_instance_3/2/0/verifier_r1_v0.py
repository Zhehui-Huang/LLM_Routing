import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, claimed_cost):
    # City coordinates
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
        (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    # Check if the tour starts and ends at the depot (Requirement 1 and Requirement 4)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except the depot city (Requirement 2)
    visited = set(tour)
    all_cities = set(range(20))
    if visited != all_cities or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate the total travel cost (Requirement 3 and Requirement 5)
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        coord1 = coordinates[city1]
        coord2 = coordinates[city2]
        total_calculated_cost += euclidean_distance(coord1[0], coord1[1], coord2[0], coord2[1])

    # Compare claimed travel cost with calculated travel cost
    if not math.isclose(total_calculated_cost, claimed_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Your provided tour and cost
tour = [0, 3, 19, 6, 13, 2, 5, 17, 15, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.36719998557066

# Verify the solution
verification_result = verify_solution(tour, total_travel_cost)
print(verification_result)