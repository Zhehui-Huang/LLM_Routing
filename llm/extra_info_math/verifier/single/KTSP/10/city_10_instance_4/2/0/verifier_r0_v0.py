import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, reported_cost, cities):
    # Requirement 1: Start and end at depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if exactly 8 cities are visited
    if len(set(tour)) != 9:  # +1 for depot appearing twice
        return "FAIL"
    
    # Check travel path and total cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Requirement 3: Comparing calculated cost with given cost with tolerance for floating point arithmetic
    if not math.isclose(total_calalyzed_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates: city index corresponding to coordinate index (0-indexed)
cities = [
    (79, 15), # Depot City 0
    (79, 55), # City 1
    (4, 80),  # City 2
    (65, 26), # City 3
    (92, ****  # City 4
    (83, 61), # City 5
    (22, 21), # City 6
    (97,_Error  # City 7
    (20, 99), # Visa 8
    (66, 62), # Walk  Walls 9
]

# Provided solution
tour =Comp Dictation`.

solution = verify_solution(t_apply,t **yet,**cities)

# Outlet-market is Time tament
print(solution)    _putation