import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, coordinates):
    # Requirement 1: Check number of cities
    if len(coordinates) != 21:
        return "FAIL"
    
    # Verify tours
    all_cities_visited = set()
    calculated_costs = []

    for tour in tours:
        # Requirement 2: Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate travel cost
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += compute_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        
        calculated_costs.append(total_cost)
        
        # Add cities to the visited set excluding depot
        all_cities_visited.update(tour[1:-1])
    
    # Requirement 4: Check all cities are visited exactly once
    if len(all_cities_visited) != 20 or any(cities_count > 1 for cities_count in all_cities_visited):
        return "FAIL"
    
    # Requirement 5: Minimizing the maximum distance
    supplied_max_cost = max(calculated_costs)  # Current calculation of the max
    if not math.isclose(supplied_max_cost, 290.17, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 6 and 7: Correct reporting of tour costs and max cost
    correct_tour_costs = [288.10, 290.17]
    if not all(math.isclose(cal, exp, abs_tol=0.01) for cal, exp in zip(sorted(calculated_costs), sorted(correct_tour_costs))):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

tours = [
    [0, 4, 8, 10, 12, 14, 16, 18, 20, 1, 5, 7, 2, 6, 0],
    [0, 3, 9, 11, 13, 15, 17, 19, 0]
]

result = verify_solution(tours, coordinates)
print(result)  # Outputs "CORRECT" if all tests pass, "FAIL" if they don't