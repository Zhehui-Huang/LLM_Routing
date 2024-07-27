import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tour, total_cost_claimed):
    # Define the cities with their coordinates
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }

    # Verify the number of cities
    if len(set(tour)) - 1 != len(cities) - 1 or set(tour) != set(range(10)):
        return "FAIL"

    # Verify if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the actual travel cost using Euclidean distances
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Compare the claimed total cost with the computed actual cost
    if abs(actual_cost - total_cost_claimed) > 0.01:  # Allowing a small discrepancy due to floating-point arithmetic
        return "FAIL"

    return "CORRECT"

# Provided solution specs
tour_test = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
total_cost_test = 354.91

# Execute the test
print(verify_solution(tour_test, total_cost_test))