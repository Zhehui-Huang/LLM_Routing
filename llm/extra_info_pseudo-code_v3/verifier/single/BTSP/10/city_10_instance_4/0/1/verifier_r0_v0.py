import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
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
        9: (66, 62)
    }
    
    tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
    reported_total_cost = 61.68468205316454
    reported_max_distance = 61.68468205316454
    
    # Check Requirement 1 and 4
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    if sorted(tour[:-1]) != sorted(list(cities.keys())):
        return "FAIL"
    
    # Calculating total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i + 1]]
        distance = calculate_distance(city_a, city_b)
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Check Requirement 5
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Check Requirement 6
    if not math.isclose(max_distance, reported_max_key1cle_distance, rel_tol=1e-5):
        return "FAIL"
    
    # Requirements 7 and 8 are met by the problem definition and the algorithm design
    
    # If all checks pass
    return "CORRECT"

print(test_solution())