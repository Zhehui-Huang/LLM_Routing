import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    correct = 'CORRECT'
    fail = 'FAIL'
    
    # Check if exactly 6 cities are visited
    if len(set(tour)) != 6 or len(tour) != 7:
        return fail
    
    # Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return fail
    
    # Calculate the total travel cost in the provided tour and compare with the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return fail
    
    return correct

# Data setup
cities = {0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)}
tour = [0, 8, 5, 2, 1, 9, 0]
total_cost = 183.85354044487238

# Test the solution
result = verify_solution(tour, total_cost, cities)
print(result)