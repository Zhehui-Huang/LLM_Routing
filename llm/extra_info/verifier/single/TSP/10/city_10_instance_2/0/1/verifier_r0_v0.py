import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates):
    # Check if the tour starts and ends at the depot, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Check if there are 10 cities in total including the depot
    if len(city_coordinates) != 10:
        return "FAIL"

    # Calculate the travel cost and compare with the given total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-4):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Given cities coordinates {city_index: (x, y)}
cities_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Provided tour and total travel cost
tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
total_cost = 384.7863591860825

# Verify the solution
result = verify_solution(tour, total_cost, cities_coordinates)
print(result)