import math

# Define the coordinates of each city in a list of tuples
cities_coordinates = [
    (29, 51),  # City 0: Depot
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

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x_diff = cities_coordinates[city1][0] - cities_types_coordinates[city2][0]
    y_diff = cities_coordinates[city1][1] - cities_coordinates[city2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Proposed solution
tour = [0, 9, 3, 7, 1, 6, 13, 2, 8, 14, 11, 12, 4, 10, 5, 0]
total_travel_cost = 437.63
max_distance = 83.43

# Unit tests
def test_solution(tour, total_travel_cost, max_distance):
    # Test Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test Requirement 2
    unique_cities = set(tour)
    if len(unique_cities) != 16 or 0 in unique_cities and len(unique_cities) - 1 != len(cities_coordinates):
        return "FAIL"
    
    # Test Requirement 5
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test Requirement 6 and 7
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(tour[i-1], tour[i])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    if not (abs(calculated_total_cost - total_travel_cost) < 0.01 and
            abs(calculated_max_distance - max_distance) < 0.01):
        return "FAIL"
    
    # Requirement 8: Can't be tested programmatically without implementation details of the algorithm
    return "CORRECT"

# Run tests and output result
print(test_solution(tour, total_travel_cost, max_distance))