import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost_provided):
    # Given coordinates of the cities with depot city 0
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 
        4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2), 
        8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 
        12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 
        16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 16 cities are visited (17 entries in the tour, including the repeated depot city)
    if len(set(tour)) != 16 or len(tour) != 17:
        return "FAIL"
    
    # Calculate the total cost from the provided tour
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the provided total cost matches the calculated cost (allowing for minor floating-point discrepancies)
    if not math.isclose(total_cost_calculated, total_cost_provided, rel_tol=1e-5):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 10, 0]
total_cost = 280.69500045619816

# Verify the solution
result = verify_solution(tour, total_cost)
print(result)