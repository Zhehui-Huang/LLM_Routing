import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, total_cost):
    # Requirement 1: Verify exactly 4 cities are visited including the depot
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"

    # Requirement 2: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate travel cost and check with given total cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    # Requirement 3 & 5: Check calculated distance against provided total distance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Given city coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Provided solution
solution_tour = [0, 1, 10, 8, 0]
solution_cost = 90.53947981328088

# Verify solution
print(verify_tour(cities, solution_tour, solution_cost))