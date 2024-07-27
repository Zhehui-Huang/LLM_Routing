import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour_solution():
    # Data given as part of the solution
    tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 10, 15, 4, 3, 6, 19, 0]
    expected_total_cost = 408.57
    expected_max_distance = 79

    # Coordinates for each city, including the depot as the first (index 0)
    city_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), (47, 50),
        (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
        (64, 72), (14, 89)
    ]

    # Calculating the total cost of travel and the max distance between consecutive cities
    current_total_cost = 0
    current_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        current_total_cost += distance
        current_max_distance = max(current_max_distance, distance)

    # Adjust to two decimal places as per expected output
    current_total_cost = round(current_total_cost, 2)

    # Checking requirements
    if tour[0] != 0 or tour[-1] != 0:  # Requirement 1 and Requirement 5
        return "FAIL"
    if sorted(tour) != sorted(list(range(20)) + [0]):  # Requirement 2
        return "FAIL"
    if abs(current_total_cost - expected_total_cost) > 0.01:  # Requirement 6
        return "FAIL"
    if not (current_max_distance <= expected_max_distance):  # Requirement 4
        return "FAIL"

    # IF all checks are passed, the solution is correct
    return "CORRECT"

# Output the result of the test (CORRECT or FAIL)
test_result = test_tour_solution()
print(test_result)