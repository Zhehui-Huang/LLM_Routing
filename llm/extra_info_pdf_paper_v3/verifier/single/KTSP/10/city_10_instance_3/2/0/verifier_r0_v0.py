import math

def euclidean_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(tour, coordinates):
    """
    Calculate the total travel cost of a tour based on given city coordinates.
    """
    total_distance = 0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        total_distance += euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return total_distance

def verify_solution(tour, total_cost_expected, coordinates, expected_city_count):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes exactly the expected number of cities
    if len(tour) != expected_city_count + 1:  # include start/end city
        return "FAIL"
    
    # Check if the total distance matches the given total cost
    calculated_total_distance = calculate_total_distance(tour, coordinates)
    if not math.isclose(calculated_total_distance, total_cost_expected, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates with the depot as the first element (city 0)
coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Given solution tour and cost
solution_tour = None  # This should be a list like [0, 1, 2, 3, 4, 5, 6, 0], now it's None, that's not correct
solution_total_cost = 159.97188184793015

# Verify the solution
if solution_tour is not None:
    result = verify_solution(solution_tour, solution_total_cost, coordinates, 7)
else:
    result = "FAIL"

print(result)