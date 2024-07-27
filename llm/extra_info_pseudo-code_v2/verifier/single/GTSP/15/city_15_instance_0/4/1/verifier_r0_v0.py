import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # The cities coordinates
    cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
              (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
              (3, 21), (60, 55), (4, 39)]

    # City groups
    groups = [
        [2, 7, 10, 11, 14],      # Group 0
        [1, 3, 5, 8, 13],        # Group 1
        [4, 6, 9, 12]            # Group 2
    ]
    
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0] * 3
    for index in tour:
        for group_id, group in enumerate(groups):
            if index in group:
                visited_groups[group_id] += 1
                if visited_groups[group_id] > 1:  # More than one city from same group visited
                    return "FAIL"
    if not all(v == 1 for v in visited_groups):  # Not all groups are visited exactly once
        return "FAIL"
    
    # Calculate travel cost and compare with given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        start = cities[tour[i]]
        end = cities[tour[i + 1]]
        calculated_cost += euclidean_distance(*start, *end)
    
    # Tolerate minor floating-point precision issues in cost comparison
    if abs(calculated_cost - total_cost) > 0.001:
        return "FAIL"
    
    return "CORRECT"

# Given solution for verification
given_tour = [0, 10, 1, 9, 0]
given_total_cost = 122.22

# Verify the solution and print the result
print(verify_solution(given_tour, given_total_cost))