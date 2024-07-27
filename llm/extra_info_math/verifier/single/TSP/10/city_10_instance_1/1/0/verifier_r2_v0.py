import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, total_cost):
    # Requirements check: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement check: Visit all other cities exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Requirement check: Travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Using a tolerance value to handle floating point precision issues
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-03):
        return "FAIL"
    
    # If all checks pass, then the solution is correct
    return "CORRECT"

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

tour = [0, 6, 1, 7, 9, 2, 5, 3, 8, 4, 0]
total_cost = 278.93

# Conduct the verification
result = verify_tour(cities, tour, total_cost)
print(result)