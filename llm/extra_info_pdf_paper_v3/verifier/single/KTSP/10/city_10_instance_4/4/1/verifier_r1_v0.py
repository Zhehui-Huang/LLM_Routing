import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, cities):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the tour visits exactly 8 cities including the depot
    if len(set(tour)) != 8 or len(tour) != 9:
        return "FAIL"
    
    # Verify the cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given cities coordinates
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

# Given solution
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost = 235.37735391753955

# Verify the solution
result = verify_solution(tour, total_travel_cost, cities)
print(result)