import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution(tour, provided_total_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
        (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
        (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Check requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2
    visited_cities = set(tour)
    if len(visited_cities) != len(cities) or visited_cities != set(range(len(cities))):
        return "FAIL"
    
    # Check requirement 4
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check requirement 3 and requirement 5
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        actual_total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Allow small floating point discrepancies in cost comparison
    if not math.isclose(provided_total_cost, actual_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_travel_cost = 410.03585920085146

# Run the test
result = verify_solution(tour, total_travel_cost)
print(result)