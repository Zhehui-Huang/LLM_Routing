import math

# Robot tour solution given
solution_tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
solution_total_cost = 477.0516251264448
solution_max_distance = 87.45856161634491

# Defined cities and their positions
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

def calculate_euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Verify tour start and end
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify each city is visited once
    if sorted(tour[:-1]) != sorted(cities.keys()):
        return "FAIL"

    # Calculate tour cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)

    # Verify total travel cost
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-6):
        return "FAIL"

    # Verify maximum distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Use the function to verify the solution
result = verify_solution(solution_tour, solution_total_cost, solution_max_distance)
print(result)