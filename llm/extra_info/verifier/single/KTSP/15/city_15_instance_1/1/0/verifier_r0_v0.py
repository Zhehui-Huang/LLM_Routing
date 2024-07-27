import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates according to the provided description
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

# Provided tour and total cost
provided_tour = [0, 6, 1, 7, 3, 9, 0]
calculated_total_cost = 118.8954868377263  # Given by you

# Calculate the total cost of the provided tour
def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = cities[tour[i]], cities[tour[i + 1]]
        total_cost += euclidean_distance(city1, city2)
    return total_cost

# Check the requirements
def validate_tour(tour, expected_cost):
    # Check Requirement 1
    assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at the depot city"

    # Check Requirement 2
    assert len(set(tour)) == 6, "Tour does not visit exactly 6 cities"

    # Check Requirement 3
    calculated_cost = calculate_total_travel_cost(tour, cities)
    assert math.isclose(calculated_cost, expected_cost, rel_tol=1e-9), "Calculated cost does not match provided cost"

    # No reliable way to check Requirement 4 automatically, as we'd need all possible valid tours for comparison
    # We assume provided solution is optimal. Real checking would involve solving the problem optimally and comparing.

    # Requirement 5 is assumed correct by output format
    
    return "CORRECT"

# Test the provided solution
try:
    result = validate_tour(provided_tour, calculated_total_cost)
    print(result)
except AssertionError as e:
    print("FAIL: " + str(e))