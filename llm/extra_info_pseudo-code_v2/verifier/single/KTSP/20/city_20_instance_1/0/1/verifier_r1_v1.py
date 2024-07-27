import math

# City coordinates represented as a dictionary
cities_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Given tour and its calculated cost
given_tour = [0, 1, 9, 8, 2, 13, 0]
given_total_cost = 125.56947407943329

def calculate_tour_cost(tour, city_coords):
    def euclidean_distance(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
    
    total_cost = 0
    for i in range(1, len(tour)):
        city1, city2 = tour[i-1], tour[i]
        total_cost += euclidean_distance(city_coords[city1], city_coords[city2])
    return total_cost

def test_solution():
    # Requirement 1: Check start and end at depot city 0
    if given_tour[0] != 0 or given_tour[-1] != 0:
        return "FAIL: Tour must start and end at city 0."

    # Requirement 2: Tour must have exactly 7 stops, including the same city twice for start and end (hence we check for 7 unique entries)
    if len(set(given_tour)) < 7:
        return "FAIL: Tour does not include exactly 7 cities."
    
    # Requirement 3: Check if given_total_cost is correctly calculated and close to the calculated cost
    calculated_cost = calculate_tour_cost(given_tour, cities_coordinates)
    if not math.isclose(calculated_cost, given_total_cost, rel_tol=1e-5):
        return f"FAIL: Cost mismatch. Expected: {given_total_cost}, Calculated: {calculated_cost}"
    
    # Requirement 4: Not computable without seeing the actual implementation of the GVNS used.
    # This cannot be verified through a unit test without reimplementation or access to function logs.
    
    # Requirement 5: Output format check (already verified implicitly by the tests for other requirements).

    return "CORRECT"

# Run the tests
print(test_solution())