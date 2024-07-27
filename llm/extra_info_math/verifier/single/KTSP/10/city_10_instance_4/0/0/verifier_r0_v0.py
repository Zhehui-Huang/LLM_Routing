import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution(tour, cost_solution):
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 8:
        return "FAIL"
    
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_calculated_cost, cost_solution, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 1, 3, 4, 5, 7, 8, 9, 0]
total_cost = 363.60

# Run test
result = test_solution(tour, total_cost)
print(result)