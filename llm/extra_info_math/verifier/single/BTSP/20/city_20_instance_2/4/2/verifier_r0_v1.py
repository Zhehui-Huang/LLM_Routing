import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the city coordinates as per the environment information
cities = {
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

# Provided solution
provided_tour = [0, 19, 12, 14, 16, 13, 9, 2, 15, 18, 5, 1, 17, 3, 4, 7, 6, 8, 10, 11, 0]
provided_total_cost = 589.7653712547985
provided_max_distance = 41.593268686170845

# Check if every city (except the depot city which is visited twice, start and end) is visited exactly once
unique_visits = set(provided_tour[1:-1])
if len(unique_visits) == 19 and provided_tour[0] == provided_tour[-1] == 0:
    visit_test = True
else:
    visit_test = False

# Calculate the total travel cost and maximum distance between consecutive cities from the provided tour
calculated_total_cost = 0
max_distance = 0

for i in range(len(provided_tour) - 1):
    dist = euclidean_distance(cities[provided_tour[i]], cities[provided_tour[i + 1]])
    calculated_total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Check the rounded values to avoid floating point representation issues
calculated_total_cost = round(calculated_total_cost, 10)
provided_total_cost = round(provided_total_cost, 10)
max_distance = round(max_distance, 10)
provided_max_distance = round(provided_max_distance, 10)

# Validate the calculated costs and distances against provided values
cost_test = calculated_total_cost == provided_total_cost
max_distance_test = max_distance == provided_max_distance

# Print test results
if visit_test and cost_test and max_distance_test:
    print("CORRECT")
else:
    # Display which tests failed, for debugging purposes
    failed_tests = []
    if not visit_test:
        failed_tests.append("visit")
    if not cost_test:
        failed_tests.append("cost")
    if not max_distance_test:
        failed_tests.append("max_distance")
    print("FAIL - Tests failed:", failed_tests)