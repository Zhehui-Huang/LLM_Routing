import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_cost += euclidean_distance(cities[city1], cities[city2])
    return total_cost

def test_solution():
    # Define city coordinates
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
        9: (66, 62),
    }
    
    # Provided solution
    tour = [0, 4, 7, 5, 1, 9, 2, 3, 0]
    reported_cost = 277.97
    
    # Verifications
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    if len(set(tour)) != 9: # 8 unique cities plus the depot
        return "FAIL"
    
    # [Requirement 3]
    calculated_cost = calculate_total_travel_cost(cities, tour)
    if not math.isclose(reported_cost, calculated_cost, abs_tol=0.01):
        return "FAIL"
    
    # [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 6]
    if not math.isclose(calculated_cost, reported_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

print(test_solution())