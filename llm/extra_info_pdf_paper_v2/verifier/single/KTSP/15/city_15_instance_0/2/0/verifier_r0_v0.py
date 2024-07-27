import math

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates as given
    cities = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 59),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }
    
    # Verify start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 4 unique cities including the depot
    if len(set(tour)) != 4:
        return "FAIL"
    
    # Verify total cost calculation
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1, city2 = tour[i], tour[i+1]
        calculated_cost += calculate_euclidean_distance(cities[city1], cities[city2])
    
    # Check calculated cost rounded to 2 decimals against provided total cost
    if abs(round(calculated_cost, 2) - total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Provided solution tour and cost
solution_tour = [0, 1, 10, 8, 0]
solution_total_cost = 90.54

# Verify the solution
verification_result = verify_solution(solution_tour, solution_total_cost)
print(verification_result)