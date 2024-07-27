import math

# Define the function to calculate Euclidean distance between two points (cities)
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of each city including the depot
cities = [
    (3, 26),   # Depot
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Tour result from the MILP solution
tour = [0, 12, 19, 18, 11, 6, 8, 10, 3, 4, 17, 1, 5, 15, 2, 9, 13, 16, 7, 14, 0]
# Expected total travel cost and maximum travel distance
expected_total_cost = 516.41
expected_max_distance = 41.59

# Function to verify the solution
def verify_solution(tour, expected_total_cost, expected_max_distance):
    # Check if all cities are visited exactly once and tour starts/ends at the depot
    if sorted(tour[:-1]) != sorted(list(range(20))):
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Compute total travel cost and the maximum distance between consecutive cities in the tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        max_distance = max(max_distance, dist)

    # Check if computed values match expected values within a reasonable tolerance
    if abs(total_cost - expected_total_cost) > 0.1 or abs(max_distance - expected_max_distance) > 0.1:
        return "FAIL"

    return "CORRECT"

# Output the result of the verification
result = verify_solution(tour, expected_total_cost, expected_max_distance)
print(result)