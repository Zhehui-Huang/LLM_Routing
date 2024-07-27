import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, max_distance_between_cities):
    # Coordinates of cities from the problem statement
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return 'FAIL'
    
    # Requirement 2: Visit each city exactly once
    if len(tour) != 16 or len(set(tour)) != 16:
        return 'FAIL'

    # Requirement 5: Check the correctness of the reported travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        dist = euclidean_distance(x1, y1, x2, y2)
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-9):
        return 'FAIL'
    if not math.isclose(calculated_max_and_distance, max_distance_between_cities, rel_tol=1e-9):
        return 'FAIL'
    
    # If all checks pass
    return 'CORRECT'

# Inputs from the provided solution
tour_solution = [0, 5, 0]
total_travel_cost_solution = float('inf')
max_distance_between_cities_solution = 12.529964086141668

# Verify the solution
result = verify_solution(tour_solution, total_travel_cost_solution, max_distance_between_cities_solution)
print(result)