import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    # City coordinates
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    
    # 1. Check if all cities except the depot are visited exactly once
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # 2. Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # 3. Calculate the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # 4. Check if the calculated cost matches the given total cost within a small error margin, due to floating-point arithmetic
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.001):
        return "FAIL"
    
    # 5. Check tour validity (already covered if all other tests pass)
    
    return "CORRECT"

# Solution provided
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_cost = 373.61498801130097

# Execute test
result = test_solution(tour, total_cost)
print(result)