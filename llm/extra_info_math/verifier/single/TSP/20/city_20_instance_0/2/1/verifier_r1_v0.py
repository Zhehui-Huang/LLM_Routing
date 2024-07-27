import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

tour = [0, 16, 14, 7, 12, 9, 11, 15, 18, 3, 10, 2, 6, 19, 5, 17, 13, 8, 1, 4, 0]
reported_cost = 349.19740471955487

def test_robot_tour(tour, cities, reported_cost):
    # [Requirement 1] Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if every city is visited exactly once (excluding depot which should be visited twice)
    from collections import Counter
    city_counts = Counter(tour)
    if city_counts[0] != 2 or any(city_counts[city] != 1 for city in range(1, 20)):
        return "FAIL"
    
    # [Requirement 3] Already verified by tests for Requirement 1
    
    # [Requirement 4] Check correct calculation of total travel cost based on Euclidean distance
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run tests
test_result = test_robot_tour(tour, cities, reported_cost)
print(test_result)