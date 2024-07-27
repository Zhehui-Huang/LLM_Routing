import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (9, 93),  # city 0
    (8, 51),  # city 1
    (74, 99), # city 2
    (78, 50), # city 3
    (21, 23), # city 4
    (88, 59), # city 5
    (79, 77), # city 6
    (63, 23), # city 7
    (19, 76), # city 8
    (21, 38), # city 9
    (19, 65), # city 10
    (11, 40), # city 11
    (3, 21),  # city 12
    (60, 55), # city 13
    (4, 39)   # city 14
]

solution_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
reported_total_cost = 373.97
reported_max_dist = 63.60

def test_tour(tour, cities):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    actual_max_dist = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        actual_max_dist = max(actual_max_dist, distance)
    
    # Check against reported values
    if not math.isclose(total_cost, reported_total_cost, rel_tol=0.01) or not math.isclose(actual_max_dist, reported_max_dist, rel_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

result = test_tour(solution_tour, cities)
print(result)