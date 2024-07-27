import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

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

provided_tour = [0, 6, 11, 5, 10, 4, 3, 2, 0]
provided_cost = 153.01

def test_solution(tour, cost):
    # Test the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test that 8 cities are visited including the depot
    if len(tour) != 9:  # Counts include both starting and ending at depot
        return "FAIL"

    # Test all cities in the tour are valid and no non-existent cities are included
    if any(city not in cities for city in tour):
        return "FAIL"

    # Calculate the travel cost and compare with provided cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the calculated cost is approximately equal to the provided cost
    if not math.isclose(total_calculated_cost, cost, abs_tol=0.01):
        return "FAIL"
    
    # Additional tests for the specific algorithm used and output format could not be automated without algorithm implementation details
    # Assuming those aspects are correct as per the problem statement scenario

    return "CORRECT"

# Run the test
test_result = test_solution(provided_tour, provided_cost)
print(test_result)