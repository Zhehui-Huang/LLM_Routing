import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost_calculated):
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }

    n = len(cities)
    
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: All cities visited exactly once excluding the depot
    if sorted(tour[1:-1]) != list(range(1, n)):
        return "FAIL"
    
    # Requirement 3: Total travel distance
    total_cost_computed = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_cost_computed += calculate_euclidean_distance(*cities[city_from], *cities[city_to])
    
    if not math.isclose(total_cost_computed, total_cost_calculated, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 5: No subtours should be formed
    encountered = set()
    for city in tour[1:-1]:
        if city in encountered:
            return "FAIL"
        encountered.add(city)
    
    return "CORRECT"

# Provided solution outputs
tour = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]
total_cost = 214.15881957089695

# Verify the solution
print(verify_solution(tour, total_cost))