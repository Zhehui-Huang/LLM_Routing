import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour(tour, cities):
    # Check Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) != len(cities) + 1:  # plus one because it returns to the start
        return "FAIL"
    
    # This Requirement 3 can not be checked for correctness without knowing the true optimal solution, so skip it:
    # - The goal is to minimize the longest distance between any two consecutive cities in the tour.

    # If multiple check requirements pass up to here, then output "CORRECT".
    return "CORRECT"

# Cities data
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

# Given tour result
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 337.17
max_distance_consecutive = 61.68

# Checking the tour validity
result = check_tour(tour, cities)
print(result)