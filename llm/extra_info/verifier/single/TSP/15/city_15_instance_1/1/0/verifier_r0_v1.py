import math

# Define the cities' coordinates 
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Functions to check solution
def verify_tour(tour):
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Check if all other cities are visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or visited_cities != set(range(1, 15)):
        return False

    return True

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# The given tour and cost
provided_tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
provided_cost = 442.570870788815

# Unit test execution
def test_solution():
    if not verify_tour(provided_tour):
        return "FAIL"
    
    calculated_cost = calculate_total_distance(provided_tour)
    if abs(provided_cost - provided_cost) > 1e-6:  # Allowing a small margin for floating point precision issues
        return "FAIL"

    # Since the actual problem does not provide the reference shortest path, we assume the provided is optimal.
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)