import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    # Check Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit each city exactly once (excluding depot city, visited twice at start and end)
    unique_cities = set(tour)
    if len(unique_cities) != 11 or len(tour) != 11:
        return "FAIL"

    # Check Requirement 3: Minimize the longest distance between consecutive cities
    # Calculate all distances between consecutive cities in the tour
    consecutive_distances = [euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)]
    
    # Identify the maximum consecutive distance
    max_distance = max(consecutive_distances)
    
    # The reported max distance is correct
    if abs(max_distance - 56.61271941887264) > 0.001:  # Allowing a little tolerance
        return "FAIL"

    return "CORRECT"

# Given city coordinates
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

# Defined tour from the optimization output
tour = [0, 6, 1, 7, 9, 2, 5, 3, 4, 8, 0]

# Verify the tour solution
correctness = verify_solution(tour, cities)
print(correctness)