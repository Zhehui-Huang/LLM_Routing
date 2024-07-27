import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cost):
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
        4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
        8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
        12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # [Requirement 1] Check if the tour visits exactly 12 cities and starts/ends at the depot city (0)
    if len(tour) != 13 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check for duplicate visits to cities other than the depot city
    city_visit_counts = {i: 0 for i in range(len(cities))}
    for city in tour:
        city_visit_counts[city] += 1
    
    if any(count > 1 for i, count in city_visit_counts.items() if i != 0) or city_visit_counts[0] != 2:
        return "FAIL"

    # [Requirement 2] & [Requirement 3] - Check the calculated distance
    calc_cost = 0
    for i in range(len(tour) - 1):
        calc_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calc_cost, cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution and cost
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 0]
cost = 241.29

# Verification result
result = verify_solution(tour, cost)
print(result)