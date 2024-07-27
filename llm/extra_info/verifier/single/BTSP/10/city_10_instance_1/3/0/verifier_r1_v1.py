import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, total_cost, max_distance):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Requirement 1: Check if the tour starts and ends at city 0, and visits all cities exactly once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != sorted(cities.keys() - {0}):
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Requirement 4: Check the calculated total cost with the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # Requirement 5: Check the calculated max distance with the provided max distance
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 6, 1, 7, 2, 9, 5, 3, 4, 8, 0]
total_travel_cost = 295.12
maximum_distance = 56.61

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)