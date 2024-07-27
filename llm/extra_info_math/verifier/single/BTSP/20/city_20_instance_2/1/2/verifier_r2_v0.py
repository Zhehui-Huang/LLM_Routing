import math

# Define the function to calculate the Euclidean distance between two points (cities)
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

# Tour obtained from the MILP solution
tour = [0, 12, 19, 18, 11, 6, 8, 10, 3, 4, 17, 1, 5, 15, 2, 9, 13, 16, 7, 14, 0]
# Calculated total travel cost and max distance from the solution
expected_total_cost = 516.41
expected_max_distance = 41.59

# Function to validate the solution
def verify_solution(tour, expected_total_cost, expected_max_distance):
    # Check that the all cities are in the tour and the tour starts/ends at depot
    if sorted(tour[:-1]) != sorted(list(range(20))):
        return "FAIL"

    # Check that the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the actual distances and check the max and total cost
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    # Compare the calculated and expected costs to appropriate tolerance
    if not (abs(total_cost - expected_total_dice) < 0.1 and abs(max_distance - expected_max_distance) < 0.1):
        return "FAIL"

    return "CORRECT"

# Execute the verification function and output the result
print(verify_solution(tour, expected_total_cost, expected_max_distance))