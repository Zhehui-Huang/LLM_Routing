import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost(tour, expected_cost, city_coordinates):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must include exactly 8 different cities
    if len(set(tour)) != 9:  # including city 0 twice
        return "FAIL"
    
    # Requirement 3: All cities can be travelled between using Euclidean distance (implicitly guaranteed by calculation method)
    # Calculate total cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city_idx1, city_idx2 = tour[i], tour[i + 1]
        total_cost += calculate_euclidean_distance(city_coordinates[city_idx1], city_coordinates[city_idx2])
    
    # Requirement 5: Check calculated cost matches provided (within a reasonable precision due to floating point arithmetic)
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 4: A list of city indices is output (implicitly passing as it's the format given for testing)
    return "CORRECT"

# City coordinates
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

# Solution details
proposed_tour = [0, 5, 10, 3, 4, 12, 11, 6, 0]
proposed_cost = 83.77479628246256

# Execute test
result = test_tour_and_cost(proposed_tour, proposed_cost, cities)
print(result)