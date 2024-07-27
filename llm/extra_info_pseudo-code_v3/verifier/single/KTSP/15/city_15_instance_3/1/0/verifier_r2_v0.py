import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # List of city coordinates
    coordinates = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    # Requirement 1: Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if exactly 10 cities are visited and unique
    if len(tour) != 11 or len(set(tour)) != 11:
        return "FAIL"

    # Requirement 5: Ensuring format that starts and ends with the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total distance from tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    # Requirement 6: Total travel cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # If all tests are passed
    return "CORRECT"

# Example solution provided
tour_example = [0, 5, 7, 3, 12, 10, 8, 9, 14, 13, 0]
total_cost_example = 251.01491347965202
result = verify_solution(tour_example, total_cost_example)
print(result)  # Expected output: "CORRECT"