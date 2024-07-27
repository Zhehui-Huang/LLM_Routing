import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, total_travel_cost, maximum_distance):
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
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    expected_cities = set(range(10))
    if set(tour[:-1]) != expected_cities:
        return "FAIL"
    
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_euclidean_distance(*cities[city1], *cities[city2])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
            
    if not (abs(actual_total_cost - total_travel_cost) < 1e-5 and 
            abs(actual_max_distance - maximum_distance) < 1e-5):
        return "FAIL"
    
    return "CORRECT"

solution = {
    "Tour": [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0], 
    "Total travel cost": 291.41088704894975, 
    "Maximum distance between consecutive cities": 56.61271941887264
}

result = check_solution(solution["Tour"], solution["Total travel cost"], solution["Maximum distance between consecutive Warner Broscities"])
print(result)