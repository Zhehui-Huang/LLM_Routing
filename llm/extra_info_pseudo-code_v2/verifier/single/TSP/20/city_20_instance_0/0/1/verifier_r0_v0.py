import math

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(1, len(tour)):
        city1 = tour[i-1]
        city2 = tour[i]
        total_distance += math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 +
                                    (coordinates[city1][1] - coordinates[city2][1])**2)
    return total_distance

def test_solution():
    coordinates = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
                   (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
                   (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
                   (60, 63), (93, 15)]
    provided_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
    provided_cost = 349.1974047195548
    
    # Test Requirement 1: Visit each city exactly once (except depot city should appear twice, start and end)
    if len(set(provided_tour) - {0}) != 19 or provided_tour.count(0) != 2:
        return "FAIL"
    
    # Test Requirement 2: Tour starts and ends at the depot city 0
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"

    # Test Requirement 5: Check if output is correct concerning the provided distance
    calculated_distance = calculate_total_distance(provided_tour, coordinates)
    if not math.isclose(calculated_distance, provided_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

print(test_solution())