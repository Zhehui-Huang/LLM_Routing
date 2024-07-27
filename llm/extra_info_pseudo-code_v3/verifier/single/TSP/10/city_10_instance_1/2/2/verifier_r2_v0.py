import math

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += distance
    return total_distance

def test_tour(tour, expected_cost, coordinates):
    # Requirement 1: Tour start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: All cities are visited exactly once, except depot city
    if sorted(tour) != sorted(list(set(tour))) or set(tour) != set(range(len(coordinates))):
        return "FAIL"

    # Requirement 3: Total travel distance matches the expected distance
    actual_distance = calculate_total_distance(tour, coordinates)
    if not math.isclose(actual_distance, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given coordinates and solution
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
               (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

tour = [0, 3, 8, 4, 6, 1, 7, 9, 2, 5, 0]
expected_cost = 280.8414894850646

# Run the test
result = test_tour(tour, expected_cost, coordinates)
print(result)