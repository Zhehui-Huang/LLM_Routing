import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, cost):
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
    
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once aside from depot
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Requirement 4: Tour format check
    if len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Requirement 3 and 5: Correct calculation of total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += euclidean_distance(cities[city_from], cities[city_to])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
tour = [0, 3, 8, 4, 6, 1, 7, 9, 2, 5, 0]
total_travel_cost = 280.8414894850646

# Verify and output the result
result = verify_tour(tour, total_travel_cost)
print(result)