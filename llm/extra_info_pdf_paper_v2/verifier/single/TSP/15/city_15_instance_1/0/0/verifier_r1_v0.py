import math

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities, given as (x, y) coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 1: Start and end at the depot city 0
    
    if len(tour) != len(set(tour)):
        return "FAIL"  # Requirement 2: Visit each city exactly once (apart from the depot city)
    
    if set(tour[1:-1]) != set(range(1, len(cities))):
        return "FAIL"  # Requirement 2 continued: All cities must be visited exactly once
    
    # Compute the total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Use near equality for floating point comparison
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"  # Requirement 5: Correct total travel cost
    
    # As Requirement 4 is structural and evident from the construction, no separate test needed
    
    return "CORRECT"

# Provided cities and their coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Provided solution to be tested
tour = [0, 5, 4, 10, 9, 3, 7, 1, 6, 13, 11, 12, 2, 8, 14, 0]
total_cost = 397.15749397439936

# Validate the solution
result = validate_tour(tour, total_cost, cities)
print(result)  # Output "CORRECT" if all requirements are met, otherwise "FAIL"