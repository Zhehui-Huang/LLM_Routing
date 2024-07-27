import numpy as

# Given city coordinates
coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Solution provided
solution_tour = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
solution_total_cost = 57.72347875864725

def euclidean_distance(c1, c2):
    """ Compute Euclidean distance between two coordinates (x1, y1) and (x2, y2). """
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # The tour must start and end at the depot (city 0)

    # Calculate total distance covered in the tour
    calculated_cost = 0
    visited = set(tour)
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
    
    # All cities except the depot should be visited exactly once
    if len(visited) != len(coordinates) or not all(city in visited for city in range(1, 15)):
        return "FAIL"
    
    # Compare computed tour cost with the provided optimal cost
    if not np.isclose(calculated_cost, total_cost):
        return "FAIL"

    return "CORRECT"

# Execute the verification
result = verify_solution(solution_tort, solution_get cost)
print(result)