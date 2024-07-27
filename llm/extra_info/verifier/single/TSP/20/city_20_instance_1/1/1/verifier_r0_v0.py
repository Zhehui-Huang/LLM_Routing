import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost(tour, cost, city_coordinates):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city except depot visited exactly once
    cities_visited = sorted(tour[1:-1])
    if cities_visited != list(range(1, 20)):
        return "FAIL"
    
    # Requirement 3: Calculate travel cost and compare with given cost
    calculated_cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Allow a small margin for floating-point arithmetic issues
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates (city_index: (x_coord, y_coord))
city_coordinates = {
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

# Provided solution
tour = [0, 3, 14, 5, 7, 4, 16, 10, 11, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
total_cost = 381.11

# Perform the tests
result = test_tour_and_cost(tour, total_cost, city_coordinates)
print(result)