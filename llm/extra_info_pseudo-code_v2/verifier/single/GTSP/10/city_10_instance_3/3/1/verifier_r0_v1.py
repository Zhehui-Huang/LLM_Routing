import math

def calculate_distance(city_A, city_B):
    # Correcting variable naming
    return math.sqrt((city_A[0] - city_B[0])**2 + (city_A[1] - city_B[1])**2)

def test_solution():
    # City coordinates as given in the task description
    cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
    
    # City groups as specified
    groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]
    
    # Tour solution provided
    solution_tour = [0, 7, 1, 4, 8, 5, 2, 0]
    solution_cost = 324.1817486177585
    
    # Check: Tour should start and end at the depot
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL: Tour should start and end at the depot city."
    
    # Ensure each group is visited exactly once
    visited_groups = [False] * len(groups)
    for city in solution_tour[1:-1]:  # Exclude the depot at start and end
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL: Multiple cities from a single group visited."
                visited_groups[i] = True
    
    if not all(visited_groups):
        return "FAIL: Not all groups are visited."
    
    # Calculate the actual tour cost using distances between consecutive cities
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        city_a = cities[solution_tour[i]]
        city_b = cities[solution_tour[i + 1]]
        calculated_cost += calculate_distance(city_a, city_b)
    
    # Compare the calculated tour cost with the solution cost
    if not math.isclose(calculated_cost, solution_cost, abs_tol=0.001):
        return f"FAIL: Calculated cost ({calculated_cost}) does not match provided cost ({solution_cost})."
    
    return "CORRECT"

# Execute the test function and print the result
print(test_solution())