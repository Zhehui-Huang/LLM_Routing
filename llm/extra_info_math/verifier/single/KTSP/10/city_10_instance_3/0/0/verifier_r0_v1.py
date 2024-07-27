import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    # Expected cities coordinates list
    cities = [(84, 67), (74, 40), (71, 13), (74, 82),
              (97, 28), (0, 31), (8, 62), (74, 56),
              (85, 71), (6, 76)]

    # Verify the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify the robot visits exactly 7 cities (8 including the inclusion of the depot twice)
    if len(set(tour)) != 8:
        return "FAIL"

    # Calculate the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Compare calculated total travel cost with the given total travel cost
    if abs(calculated_cost - total_travel_cost) > 0.01:  # Adding a small tolerance for floating-point arithmetic
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_travel_cost = 159.97

# Verify the solution
result = verify_solution(tour, total_travel_cost)
print(result)  # Output either "CORRECT" or "FAIL"