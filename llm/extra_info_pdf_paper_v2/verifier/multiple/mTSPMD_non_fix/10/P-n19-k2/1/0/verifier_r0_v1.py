import math

# Provided coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Robot tours and costs provided in the solution
robot_tours = [0, 18, 6, 1, 10, 3, 17, 16, 8, 9, 15, 13, 5, 7, 2, 4, 11, 14, 12]
robot_cost = 181.49265243386333

# Function to calculate Euclidean distance
def euclidean_distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Validate the solution
def validate_solution(tours, reported_cost):
    # Requirement 1: Verify all cities are visited exactly once
    all_visited = set(tours)
    if all_visited != set(range(len(cities))):
        return "FAIL: Cities visited are not matching."

    # Requirement 2: Robot 0 starts at city index 0
    if tours[0] != 0:
        return "FAIL: Robot does not start at city 0."

    # Requirement 4 and 6: Calculating travel cost and checking it
    calculated_cost = calculate_tour_cost(tours)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return f"FAIL: Cost mismatch. Expected ~{reported_cost}, calculated {calculated_cost}."

    return "CORRECT"

# Execute the validation function
test_result = validate_solution(robot_tours, robot_cost)
print(test_result)