import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_solution(tour, cost):
    # Cities coordinates
    cities = [
        (50, 42),  # 0
        (41, 1),   # 1
        (18, 46),  # 2
        (40, 98),  # 3
        (51, 69),  # 4
        (47, 39),  # 5
        (62, 26),  # 6
        (79, 31),  # 7
        (61, 90),  # 8
        (42, 49)   # 9
    ]
    
    # City groups
    groups = [
        [1, 2, 6],  # Group 0
        [3, 7, 8],  # Group 1
        [4, 5, 9]   # Group 2
    ]
    
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each city group
    visited_groups = set()
    for i in tour[1:-1]:  # exclude the depot city
        for idx, group in enumerate(groups):
            if i in group:
                visited_groups.add(idx)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Requirement 3: Travel cost is minimized
    # Calculate the travel cost from the tour
    total_computed_cost = 0
    for i in range(len(tour) - 1):
        total_computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_computed_cost, cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Example values from the provided solution
tour = [0, 7, 6, 5, 0]
cost = 72.83

# Check test results
test_result = verify_solution(tour, cost)
print(test_result)