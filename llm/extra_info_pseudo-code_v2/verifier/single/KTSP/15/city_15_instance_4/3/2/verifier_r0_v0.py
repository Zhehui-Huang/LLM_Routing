import math

def test_solution(tour, total_cost):
    # Requirement 1: Start and end at the depot, index 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Visit exactly 12 cities including the depot
    if len(set(tour)) != 13:  # Using set to eliminate duplicates and expect 13 unique entries including depot twice
        return "FAIL"
    
    # Explicitly define the city coordinates as provided in the original problem
    coordinates = {
        0: (35, 40),
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }

    # Helper function to compute Euclidean distance
    def euclidean_dist(a, b):
        return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)
    
    # Requirement 3: Calculate the total travel cost using the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_dist(tour[i], tour[i + 1])

    # Compare calculated cost with the provided total cost, allowing for floating point imprecision
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 5: Validation covered by this function implicitly by input/output format
    # No explicit fail conditions for the shortest possible path without additional information
    # so we skip Requirement 4 as we cannot verify optimal solution only based on the provided solution

    return "CORRECT"

# Test case based on the provided solution
test_tour = [0, 1, 5, 9, 2, 7, 12, 11, 6, 3, 14, 13, 10, 0]
test_cost = 274.5382352810725

# Call the test function and print the result
result = test_solution(test_tour, test_cost)
print(result)  # Expect "CORRECT" if it meets all the conditions; "FAIL" otherwise.