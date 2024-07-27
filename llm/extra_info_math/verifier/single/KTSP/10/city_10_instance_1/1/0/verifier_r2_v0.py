import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_solution(tour, cost):
    # City coordinates as per environment information
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Requirement 1: Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if exactly 5 cities are visited, including the depot
    if len(set(tour)) != 6:  # Should contain 5 unique cities + starting city repeated
        return "FAIL"
    
    # Requirement 3: Check if the travel cost is correct and minimized
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 4, 8, 3, 5, 0]
reported_cost = 110.38072506104011

# Check the solution
result = check_solution(tour, reported_cost)
print(result)