import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    coordinates = [
        (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
        (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
    ]
    
    # Test solution
    tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
    expected_total_cost = 328.3966856465968
    expected_max_distance = 45.18849411078001

    # Check starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    unique_cities = set(tour[:-1])  # Exclude the last city (depot re-entry)
    if len(unique_cities) != 10:
        return "FAIL"

    # Calculate total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        ci = tour[i]
        ni = tour[i + 1]
        distance = calculate_distance(coordinates[ci][0], coordinates[ci][1], coordinates[ni][0], coordinates[ni][1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Validate total cost and max distance
    if not math.isclose(total_cost, expected_total_cost, abs_tol=1e-6):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Run the unit test
print(test_solution())