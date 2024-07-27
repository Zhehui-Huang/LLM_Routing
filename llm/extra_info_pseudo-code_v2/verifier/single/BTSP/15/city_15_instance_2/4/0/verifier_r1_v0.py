import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city 0."
    
    if len(tour) != len(set(tour)):
        return "FAIL", "Tour visits at least one city more than once."
    
    if len(tour) != len(cities) + 1:
        return "FAIL", "Tour does not visit each city exactly once."
    
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    
    # Hardcoded expected values for the sake of this example. These should be replaced with proper calculations based on expected results.
    expected_total_distance = 100  # Example value
    expected_max_distance = 40     # Example value

    if total_distance != expected_total_distance:
        return "FAIL", "Total travel cost does not match expected."
    
    if max_distance != expected_max_distance:
        return "FAIL", "Maximum distance between consecutive cities does not match expected."

    return "CORRECT", "All tests passed."

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Simulated output from the solver
tour_simulation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]

# Run the verification test
result, message = verify_solution(tour_simulation, cities)
print("Result:", result)
print("Message:", message)