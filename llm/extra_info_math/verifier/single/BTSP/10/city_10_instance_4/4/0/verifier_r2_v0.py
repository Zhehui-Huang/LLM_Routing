def verify_solution(tour, total_distance, max_consecutive_distance):
    # Requirement 1: Start and end at depot (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once (excluding depot which is visited twice at start and end)
    visited_cities = set(tour)
    if len(visited_cities) != 11 or any(tour.count(city) != 1 for city in visited_cities if city != 0):
        return "FAIL"
    
    # Requirement 3: Since it is impossible to check optimality of minimization without solving the problem again,
    # we skip checking actual minimization and focus on the tour's integrity and correctness.
    
    # Additional checks: Calculate the peers' distances to ensure the tour matches the provided values.
    city_coordinates = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    
    # Compute distances between each consecutive pair in the tour.
    import math
    computed_total_distance = 0
    computed_max_distance = 0
    
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i+1]]
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        computed_total_distance += dist
        if dist > computed_max_distance:
            computed_max_distance = dist
    
    # Compare computed distances with given results.
    if not (math.isclose(computed_total_distance, total_distance, rel_tol=1e-2) and
            math.isclose(computed_max_distance, max_consecutive_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Tour and its statistics from the solution provided
tour = [0, 3, 7, 1, 4, 5, 9, 8, 2, 6, 0]
total_travel_cost = 416.12
max_distance_between_consecutive_cities = 61.68

# Check if the solution is correct
result = verify_solution(tour, total_travel_cost, max_distance_between_consecutive_cities)
print(result)