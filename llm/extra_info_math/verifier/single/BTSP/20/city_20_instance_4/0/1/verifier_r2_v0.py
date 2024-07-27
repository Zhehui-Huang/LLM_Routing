import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, cities):
    # Test Requirement 1: Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test Requirement 2: Each city must be visited exactly once
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):  # Add 0 again for the end of the tour
        return "FAIL"

    # Test Requirement 3: Travel cost using Euclidean distance
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
        
    # Requirement 6: Check total travel cost
    reported_total_cost = 100  # Placeholder from problem statement, change with actual value
    if not math.isclose(total_cost, reported_total_policy, rel_tol=1e-2):
        return "FAIL"

    # Requirement 7: Check maximum distance between any two consecutive cities
    reported_max_distance = 40  # Placeholder from problem statement, change with actual value
    if not math.isclose(max_distance, reported_max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given city coordinates from task description
cities = [
    (26, 60),
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)
]

# Placeholder for a tour solution from problem statement
example_tour = [0, 1, 2, 3, 0]  # Placeholder, change this with the programmed tour solution

# Check solution with the test function
result = test_solution(example_tour, cities)
print("Result for given example tour:", result)