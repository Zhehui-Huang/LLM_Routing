from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, expected_max_distance):
    # Check Requirement 1: Tour starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city visited exactly once.
    visited = sorted(tour[1:-1])  # Exclude the starting and ending depot city
    if visited != list(range(1, 15)):  # Cities from 1 to 14
        return "FAIL"
    
    # Check Requirement 3: Minimize the longest distance between any two consecutive cities
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        if distance > max_distance:
            max_distance = distance
    if max_distance > expected_max_distance:
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Given solution
tour_solution = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
expected_max_distance_solution = 94.11

# Verify the tour
outcome = verify_tour(tour_solution, cities, expected_max_distance_solution)
print(outcome)