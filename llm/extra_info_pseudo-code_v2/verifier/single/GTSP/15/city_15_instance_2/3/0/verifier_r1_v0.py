import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, cost):
    coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
        (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
        (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]
    groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]
    
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check only one city from each group is visited
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Skip the depot city in the beginning and end
        for group_index, group in enumerate(groups):
            if city in group and visited_groups[group_index]:
                return "FAIL"  # City from the same group visited more than once
            elif city in group:
                visited_groups[group_index] = True
    
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited
    
    # Calculate the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, cost, abs_tol=1e-6):
        return "FAIL"  # Incorrect total travel cost calculation
    
    return "CORRECT"

# Test input
tour = [0, 12, 10, 4, 3, 2, 0]
cost = 138.15244358342136

# Verify the solution
result = verify_solution(tour, cost)
print(result)