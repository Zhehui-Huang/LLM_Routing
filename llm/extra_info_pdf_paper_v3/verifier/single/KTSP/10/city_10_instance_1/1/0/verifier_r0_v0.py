import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 5:
        return "FAIL"
    
    expected_total_cost = 0
    for i in range(len(tour) - 1):
        expected_total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if round(expected_total_cost, 2) != total_cost:
        return "FAIL"
    
    return "CORRECT"

# Cities data
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

# Solution provided
tour = [0, 3, 4, 5, 8, 0]
total_cost = 175.37

# Verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)