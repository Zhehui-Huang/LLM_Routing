import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Verify requirement 1: Tour starts and ends at the same depot city
    if tour[0] != tour[-1]:
        return "FAIL"
    
    # Verify requirement 2: Each city is visited exactly once
    visited = set(tour)
    if len(tour) - 1 != len(visited) - 1:  # -1 because start and end are the same
        return "FAIL"
    
    # Recalculate the total cost based on the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Verify requirement 3 and 5: Calculate and check if total cost is as expected
    if not math.isclose(total_travel_cost, calculated_cost, abs_tol=1e-5):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# City coordinates for each index (including depots)
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tour given as the output of the algorithm
tour = [7, 14, 9, 13, 8, 12, 15, 11, 10, 7]
total_travel_cost = 118.50348450043907

# Verify the solution
result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)