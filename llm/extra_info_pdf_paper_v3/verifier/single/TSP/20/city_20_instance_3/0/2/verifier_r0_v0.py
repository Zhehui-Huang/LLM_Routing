import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates):
    num_cities = len(city_coordinates)

    # Requirement: Tour should start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement: Tour should have all cities exactly once, except depot visited twice (start, end)
    unique_cities = set(tour)
    if len(tour) != num_cities + 1 or len(unique_cities) != num_cities:
        return "FAIL"

    # Calculate the actual total cost based on the tour
    actual_total_cost = 0
    for i in range(1, len(tour)):
        actual_total_cost += calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
    
    # Requirement: Total cost should be correct
    if not math.isclose(actual_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given city coordinates
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Provided tour and total cost
tour = [0, 1, 5, 15, 17, 16, 9, 3, 8, 14, 7, 18, 12, 11, 10, 4, 2, 13, 6, 19, 0]
total_cost = 662.99

# Verify the solution
result = verify_solution(tour, total_cost, city_coordinates)
print(result)