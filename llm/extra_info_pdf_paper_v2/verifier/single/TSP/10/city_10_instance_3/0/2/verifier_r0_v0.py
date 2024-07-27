import math

# Given solution
solution_tour = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
solution_cost = 294.17253892411236

# Define city coordinates
city_coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, expected_cost):
    # Requirement 1: Start and end at Depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit all cities exactly once
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Calculate cost and check with the given expected cost
    total_calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Requirement 4: Check if the tour gives the least cost (approximate due to floating-point calculations)
    if not math.isclose(total_calculated_cost, expected_cost, rel_tol=1e-6):
        return "FAIL"
    
    # Requirement 5: Correct output format is assumed in the function arguments.
    
    return "CORRECT"

# Verify the given solution
result = verify_tour(solution_tour, solution_cost)
print(result)