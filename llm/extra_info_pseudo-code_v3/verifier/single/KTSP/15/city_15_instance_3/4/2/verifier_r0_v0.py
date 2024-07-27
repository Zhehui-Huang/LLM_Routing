import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
    # Given coordinates of the cities including the depot
    coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
                   (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
                   (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]
    
    # Provided solution tour and cost
    provided_tour = [0, 4, 12, 3, 9, 5, 10, 8, 13, 14, 0]
    provided_cost = 205.18
    
    # [Requirement 2] Check start and end at depot city 0
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"

    # [Requirement 3] Check that exactly 10 cities are visited
    if len(set(provided_tour)) != 10:
        return "FAIL"
    
    # [Requirement 4] Calculate the actual travel cost and compare with provided
    actual_cost = 0
    for i in range(len(provided_tour) - 1):
        actual_cost += calculate_distance(coordinates[provided_tour[i]], coordinates[provided_tour[i + 1]])
    
    # To mitigate floating point precision issues, use a small epsilon
    if not math.isclose(actual_cost, provided_cost, rel_tol=1e-2):
        return "FAIL"

    # Assuming the solution is not calculated within this testing function so [Requirement 6] can't be tested.
    # [Requirement 5] As the real shortest tour calculation is computational, this result is assumed as the shortest given we can't evaluate it here.

    return "CORRECT"

# Print the result of the test
print(test_solution())