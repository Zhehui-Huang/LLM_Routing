import math

# Function to calculate Euclidean distance
def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Data for cities provided in the setup
city_coordinates = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Solution provided
proposed_tour = [0, 2, 6, 5, 3, 7, 4, 9, 11, 1, 10, 8, 14, 12, 13, 0, 0]
proposed_cost = float('inf')  # Represented as inf

# Unit tests to verify the solution
def test_solution(tour, cost, city_coords):
    # Test Requirement 1: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test Requirement 2: Each city, except the depot, visited exactly once
    unique_cities = set(tour[1:-1])  # without considering the ending depot
    if len(unique_cities) != len(city_coords) - 1 or 0 in unique_cities:
        return "FAIL"

    # Test Requirement 5: Check the format of the tour output
    if not all(isinstance(city, int) for city in tour):
        return "FAIL"

    # Test Requirement 6: Check computed total travel cost
    computed_cost = sum(compute_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour) - 1))
    if cost != computed_cost:
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Run the test
result = test_solution(proposed_tour, proposed_cost, city_coordinates)
print(result)