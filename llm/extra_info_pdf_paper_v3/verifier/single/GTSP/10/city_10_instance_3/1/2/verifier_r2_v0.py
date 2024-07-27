import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution(tour, total_cost):
    # Coordinates of cities
    city_coordinates = [
        (84, 67),  # Depot city 0
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3
        (97, 28),  # City 4
        (0, 31),   # City 5
        (8, 62),   # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)    # City 9
    ]
    
    # Groups of cities
    groups = [
        [0],        # Depot Gorup
        [7, 9],     # Group 0
        [1, 3],     # Group 1
        [4, 6],     # Group 2
        [8],        # Group 3
        [5],        # Group 4
        [2]         # Group 5
    ]

    # Requirement 1: Tour starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = [0 for _ in groups]  # Track group visits
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
                if visited_groups[i] > 1:  # Can visit only one city per group
                    return "FAIL"
    if any(v != 1 for v in visited_groups):  # Ensure all groups are visited exactly once
        return "FAIL"
    
    # Requirement 3 and 5: Verify travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += euclidean_distance(*city_coordinates[city_a], *city_coordinates[city_b])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all tests pass
    return "CORRECT"

# Solution provided
tour = [0, 8, 4, 2, 5, 1, 7, 0]
total_cost = 257.4403135407143

# Test the solution
print(test_solution(tour, total_cost))  # Should output "CORRECT" if all validations pass