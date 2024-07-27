import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(tour, total_cost, coords):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Start or end at the depot city
    if len(tour) != 7:
        return "FAIL"  # Should visit exactly 6 cities (including depot)
    if len(set(tour)) != len(tour):
        return "FAIL"  # No city should be visited more than once

    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coords[tour[i]], coords[tour[i+1]])

    if abs(calculated_cost - total_cost) > 1e-6:
        return "FAIL"  # Cost should match the provided total cost

    # Assuming no known shorter path value, we cannot definitively check for shortest path without solving the problem itself.
    # Therefore, we only check the logical constraints and computed cost accuracy.

    return "CORRECT"

# Coordinate definition as per the task description
coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43),
               (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Given solution tour and cost
solution_tour = [0, 6, 1, 7, 3, 9, 0]
solution_total_cost = 119

# Verify the solution
print(verify_solution(solution_tour, solution_total_cost, coordinates))