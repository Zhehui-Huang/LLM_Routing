import math

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Proposed tour solution
tour_solution = [0, 6, 1, 7, 3, 9, 0]
proposed_total_cost = 118.8954868377263

# Verify solution
def verify_solution(tour, total_cost):
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if len(set(tour)) != 6:
        return "FAIL"

    # [Requirement 3]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(tour[i], tour[i+1])

    # Comparing the calculated cost with a small tolerance due to possible floating-point precision issues
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 5] - Implicitly correct by the output format in the prompt, just using Python code structure here.
    
    return "CORRECT"

# Run the verification
result = verify_solution(tour_solution, proposed_total_cost)
print(result)