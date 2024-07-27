import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Defining the city coordinates as provided in the task
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 
        15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
    }

    # Provided solution details
    tour = [0, 12, 2, 9, 19, 11, 8, 3, 4, 7, 0]
    reported_cost = 333.501091535683

    # Check Requirement 1: Tour must start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Robot needs to visit exactly 10 cities
    if len(set(tour)) != 10:
        return "FAIL"

    # Check Requirement 4: Output should list the tour starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 5: Verify the output specifies the travel cost correctly
    # We calculate the total travel cost here
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    # As Requirement 6 involves methodology and cannot be tested directly in unit test,
    # we assume it is met by verifying other output correctnesses.

    return "CORRECT"

# Run the test
print(test_solution())