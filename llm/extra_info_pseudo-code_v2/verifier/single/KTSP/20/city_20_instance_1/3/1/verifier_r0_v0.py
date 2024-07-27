import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, reported_cost, city_coordinates):
    # Check Requirement 1: Exactly 7 stops including starting and ending at the depot
    if len(tour) != 7 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 4: Output is a list starting and ending at 0
    if not isinstance(tour, list) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 6: All cities in the tour are distinct except the depot
    if len(set(tour[:-1])) != len(tour[:-1]):
        return "FAIL"
    
    # Compute the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += compute_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Check Requirement 5: Total travel cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Given city coordinates
city_coordinates = [
    (14, 77), # Depot
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Solution details
solution_tour = [0, 14, 5, 7, 9, 6, 0]
solution_cost = 135.57338992042102

# Verify the solution and print result
result = verify_solution(solution_tour, solution_cost, city_coordinates)
print(result)