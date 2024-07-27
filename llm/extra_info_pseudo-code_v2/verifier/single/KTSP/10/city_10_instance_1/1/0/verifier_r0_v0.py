import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Requirement 1 & 4: Start and end at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 5 cities including the depot
    if len(tour) != 6:  # includes starting and ending at the depot
        return "FAIL"
    
    # Requirement 4: Output should include the tour as a list of city indices, starting and ending at the depot city.
    # (Already checked with Requirement 1 & 2)
    
    # Requirement 3 & 5: Check calculated travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        city_idx1 = tour[i - 1]
        city_idx2 = tour[i]
        calculated_cost += calculate_distance(cities[city_idx1], cities[city_idx2])
    
    calculated_cost = round(calculated_cost, 2)  # matching the precision
    if calculated_cost != total_cost:
        return "FAIL"
    
    return "CORRECT"

# City positions
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 
    3: (22, 80), 4: (18, 63), 5: (54, 91), 
    6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Proposed solution
tour = [0, 4, 7, 9, 2, 0]
total_cost = 215.48

# Verification
result = verify_solution(tour, total_cost, cities)
print(result)