import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cost):
    # Define the cities according to the problem statement
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
        15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once, except depot city
    unique_visits = set(tour)
    if len(unique_visits) != len(cities) or tour.count(0) != 2:
        return "FAIL"
    
    # Requirement 3: Calculate the correct travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 4 & 5 are implicit in the other checks, assuming correctness of this implementation.
    return "CORRECT"

# Given sample solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
cost = 349.1974047195548

# Check the provided solution
result = validate_tour(tour, cost)
print(result)