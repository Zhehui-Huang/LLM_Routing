import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def validate_solution(tour, cost, cities):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 7 unique cities including the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 7 or 0 not in unique_cities:
        return "FAIL"
    
    # Requirement 3: Check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Rounding to match the cost precision given in the problem
    calculated_cost = round(calculated_cost, 2)
    if calculated_cost != cost:
        return "FAIL"
    
    return "CORRECT"

# City coordinates indexed by their numbers
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 
    17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Provided solution details
proposed_tour = [0, 0, 14, 9, 8, 13, 2, 6, 0]
proposed_cost = 130.67

# Validate the solution
result = validate_solution(proposed_tour, proposed_cost, cities)
print(result)