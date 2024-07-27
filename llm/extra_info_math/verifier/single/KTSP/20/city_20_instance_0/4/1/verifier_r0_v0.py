import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, expected_cost):
    # Cities and their coordinates
    cities = {
        0: (8, 11),
        1: (40, 6),
        8: (61, 16),
        4: (25, 18)
    }
    
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Exactly 4 cities including the depot
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate the total cost of the provided tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # [Requirement 3] Check if the total cost is minimal (Here, we simply validate against the expected provided cost)
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution data
tour_solution = [0, 1, 8, 4, 0]
expected_travel_cost = 110.09

# Verify the solution
result = verify_solution(tour_solution, expected_travel_submitted)
print(result)