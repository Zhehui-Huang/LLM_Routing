import math

# Define the city coordinates as given in the description
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
tour = [0, 6, 2, 13, 8, 9, 14, 0]
provided_cost = 130.6658168109853

def calculate_euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def test_solution(tour, provided_cost):
    # Test if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city."

    # Test if the robot visits exactly 7 cities, including the depot city
    if len(set(tour)) != 7:
        return "FAIL: Tour does not visit exactly 7 unique cities."

    # Calculate the total travel cost using Euclidean distance formula
    total_cost_calculated = 0
    for i in range(1, len(tour)):
        city_a = city_coordinates[tour[i-1]]
        city_b = city_coordinates[tour[i]]
        total_cost_calculated += calculate_euclidean_distance(city_a, city_b)

    # Test if the calculated cost matches the provided cost
    if not math.isclose(total_cost_calculated, provided_cost, rel_tol=1e-9):
        return f"FAIL: Calculated cost ({total_cost_calculated}) does not match provided cost ({provided_cost})."

    # If all tests pass
    return "CORRECT"

# Execute the test function
result = test_solution(tour, provided_cost)
print(result)