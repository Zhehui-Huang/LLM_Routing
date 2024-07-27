import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution():
    # Cities coordinates
    cities = [
        (26, 60), # City 0 - Depot
        (73, 84),
        (89, 36),
        (15, 0),
        (11, 10), # City 4
        (69, 22),
        (28, 11),
        (70, 2),
        (47, 50), # City 8
        (60, 29),
        (29, 26), # City 10
        (85, 68),
        (60, 1),
        (71, 73),
        (82, 47), # City 14
        (19, 25),
        (75, 9),
        (52, 54), # City 17
        (64, 72),
        (14, 89)  # City 19
    ]

    # Solution provided
    solution_tour = [0, 8, 17, 18, 1, 11, 14, 9, 5, 16, 7, 12, 6, 4, 15, 10, 0]
    reported_cost = 292.04

    # Verify the tour starts and ends at the depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Verify the tour visits exactly 16 distinct cities including the depot
    if len(set(solution_tour)) != 16:
        return "FAIL"
    
    # Calculate and verify the total travel cost
    total_cost = 0
    for i in range(len(solution_tour) - 1):
        total_cost += calculate_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
    
    # Comparing the calculated total cost with the reported one within a small margin for floating point arithmetic
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Running the verification function
result = verify_solution()
print(result)