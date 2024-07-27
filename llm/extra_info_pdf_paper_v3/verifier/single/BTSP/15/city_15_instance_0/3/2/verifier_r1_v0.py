import math

# Define the cities' coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Provided solution details
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost = 373.97393412233544
max_distance = 63.60031446463138

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, total_travel_cost, max_distance):
    # Check requirement 1 and 5: Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: Each city must be visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or any(city not in unique_cities for city in range(1, len(cities))):
        return "FAIL"

    # Calculate total cost and max distance to verify requirement 3, 6, and 7
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Use a tolerance for floating point comparison
    if not (math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-9) and 
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9)):
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_solution(tour, total_travel_cost, max_distance)
print(result)