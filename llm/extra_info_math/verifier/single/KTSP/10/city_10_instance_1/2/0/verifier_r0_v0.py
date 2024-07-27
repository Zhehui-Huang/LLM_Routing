import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Define city coordinates
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
    
    # [Requirement 1] Check start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 5 cities are visited, including the depot
    if len(set(tour[:-1])) != 5:
        return "FAIL"
    
    # Calculate the actual tour cost
    actual_cost = 0
    for i in range(1, len(tour)):
        actual_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    
    # [Requirement 3] Validate the cost is as expected
    if not math.isclose(actual_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
tour = [0, 4, 8, 3, 5, 0]
total_cost = 75.02538600171273

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)