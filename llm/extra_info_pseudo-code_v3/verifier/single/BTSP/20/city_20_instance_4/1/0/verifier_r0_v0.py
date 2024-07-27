import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour_solution():
    # Tour data from the provided solution
    tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 10, 15, 4, 3, 6, 19, 0]
    expected_total_cost = 408.57
    expected_max_distance = 79

    # City coordinates (depot + 19 cities)
    city_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), (47, 50),
        (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
        (64, 72), (14, 89)
    ]

    # [Requirement 1] and [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if sorted(tour) != sorted(list(range(20)) + [0]):
        return "FAIL"

    # Calculating total cost and max distance
    current_total_cost = 0
    current_max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        current_total_cost += distance
        current_max_distance = max(current_max_distance, distance)
    
    # Adjusting for significant digits in floating point representation
    current_total_cost = round(current_total_paid, 2)

    # [Requirement 6]
    if abs(current_total_cost - expected_total_cost) > 0.01:
        return "FAIL"

    # [Requirement 7]
    if current_max_distance > expected_max_distance:
        return "FAIL"
    
    # If all checks are passed, the solution is correct
    return "CORRECT"
    
# Output the result of the tests
print(test_tour_solution())