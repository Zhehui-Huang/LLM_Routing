import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_distance):
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    
    if tour is None:
        return "FAIL"
    
    # [Requirement 1] The tour must start and end at depot city (index 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The robot must visit exactly 8 cities, including the depot city.
    if len(tour) != 9:  # Includes the return to the starting city
        return "FAIL"
    
    # [Requirement 3 & 4] Validate total distance calculation
    calculated_distance = 0
    for i in range(len(tour) - 1):
        calculated_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check the accurateness of the total distance provided
    if not math.isclose(calculated_distance, total_distance, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Solution received
tour = None
total_distance = 132.12

# Checking the solution
print(test_solution(tour, total_distance))