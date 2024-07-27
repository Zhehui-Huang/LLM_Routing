import math

# Coordinates of cities
city_coordinates = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Test provided solution
solution_tour = [0, 9, 15, 5, 1, 10, 7, 11, 16, 6, 0]
provided_total_cost = 310.01

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to validate the tour and calculate its cost
def validate_and_calculate_tour_cost(tour):
    if tour[0] != 0 or tour[-1] != 0:
        return False, 0
    if len(set(tour)) != 10:
        return False, 0
    if len(tour) != 11:
        return False, 0
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return True, round(total_cost, 2)

# Unit test to check the solution
def test_solution():
    is_valid, calculated_cost = validate_and_calculate_tour_cost(solution_tour)
    if not is_valid:
        return "FAIL"
    if calculated_cost != provided_total_cost:
        return "FAIL"  # Might allow a small discrepancy for floating point comparison
    return "CORRECT"

# Run the unit test
print(test_solution())