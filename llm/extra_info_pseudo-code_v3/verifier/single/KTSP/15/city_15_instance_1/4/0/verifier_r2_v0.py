import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Coordinates of each city
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

    # Provided solution
    tour = [0, 9, 3, 7, 1, 6, 0]
    reported_cost = 118.8954868377263

    # Validate the number of cities
    if len(cities) != 15:
        return "FAIL"
    
    # Validate start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that exactly 7 cities are visited (6 unique + depot repeated)
    if len(tour) != 7:
        return "FAIL"

    # Calculate the total travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Compare reported cost with calculated cost
    if not math.isclose(reported_cost, actual_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Output the result of the tests
print(test_solution())