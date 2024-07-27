import math

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_tour(tour, total_cost_provided):
    # Coordinates for each city including depot
    cities = [
        (16, 90),  # Depot
        (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
        (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95),
        (29, 64), (32, 79)
    ]
    
    # [Requirement 2] & [Requirement 4]: Check tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1]: Check all cities are visited exactly once
    if len(set(tour)) != len(cities) or set(tour[1:-1]) != set(range(1, len(cities))):
        return "FAIL"
    
    # Compute total distance traveled
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        total_calculated_cost += calculate_euclidean_distance(city1, city2)
    
    # [Requirement 3] & [Requirement 5]: Check calculated distance matches provided total cost
    if not math.isclose(total_calculated_cost, total_cost_provided, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 14, 9, 5, 13, 6, 8, 10, 11, 2, 7, 3, 12, 4, 1, 0]
total_cost = 309.0768142248585

# Evaluate the solution
result = verify_tour(tour, total_cost)
print(result)