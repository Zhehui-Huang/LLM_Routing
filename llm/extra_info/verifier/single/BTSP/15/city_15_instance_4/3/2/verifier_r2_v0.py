import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Coordinates of each city including the depot city (city 0).
    coordinates = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Check Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit each city exactly once
    if sorted(tour) != sorted(list(set(tour))) or sorted(tour) != [i for i in range(15)] + [0]:
        return "FAIL"
    
    # Calculate the total distance and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        dist = compute_euclidean_distance(*coordinates[tour[i-1]], *coordinates[tour[i]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
    
    # Check Result Accuracy in terms of costs and distance
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-9) or \
       not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Solution details
solution_tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
solution_cost = 337.8447016788252
solution_max_distance = 60.67124524847005

# Verify the solution
result = verify_solution(solution_tour, solution_cost, solution_max_distance)
print(result)