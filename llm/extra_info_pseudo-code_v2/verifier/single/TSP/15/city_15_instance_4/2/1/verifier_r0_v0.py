import math

# Here are the city coordinates
cities_coordinates = [
    (35, 40),  # Depot City 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0]) ** 2 + (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

# Test data from the purported solution
tour_solution = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
reported_total_cost = 731.838140249715

def verify_tour(tour, reported_cost):
    # Checking Requirement 1: Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking Requirement 2: All cities visited once, except depot
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities_coordinates) - 1 or len(tour[1:-1]) != len(cities_coordinates) - 1:
        return "FAIL"
    
    # Checking Requirement 3: Travel cost calculation using Euclidean distance
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"  # There could be precision issues
    
    # Requirement 4 is related to output format, which isn't checked in this function,
    # as the format is followed in the scenario's output setup.
    
    # Requirement 5 (checking Lin-Kernighan implementation) is not verifiable just through the output,
    # as it refers to the use of a specific algorithm in the description. Assumed correct in this context.
    
    # All checks passed
    return "CORRECT"

# Testing the verification
result = verify_tour(tour_solution, reported_total_cost)
print(result)