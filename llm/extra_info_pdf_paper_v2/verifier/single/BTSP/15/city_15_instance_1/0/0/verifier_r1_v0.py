import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, cities):
    # Requirement 1: Start and end at depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Each city visited once, except depot which is visited twice
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Requirement 3: Verify maximum distance between consecutive cities
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        if dist > max_distance:
            max_distance = dist
    expected_max_distance = 83.43260753446461
    if abs(max_distance - expected_max_distance) > 0.0001:  # allowing slight precision differences
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (29, 51),  # Depot City 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Proposed solution tour
tour = [0, 4, 10, 5, 9, 3, 7, 1, 6, 13, 2, 8, 14, 11, 12, 0]

# Perform the test
result = check_solution(tour, cities)
print(result)