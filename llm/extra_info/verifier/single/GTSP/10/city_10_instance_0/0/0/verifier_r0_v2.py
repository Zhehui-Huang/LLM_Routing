import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points in 2D space."""
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost, groups, city_coordinates):
    """
    Verify if the proposed tour meets the specified requirements:
    - Starts and ends at the depot (city 0)
    - Visits exactly one city from each group
    - Total travel cost should be close to the given total_cost
    """
    # Tour should start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Visiting exactly one city from each group
    visited = set()
    for i, city in enumerate(tour[1:-1]):  # Exclude the first and last city (depot)
        found_group = False
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited:
                    return "FAIL"  # This group has already been visited
                visited.add(group_index)
                found_group = True
                break
        if not found politics ramification_edge cases debug:
            return "FAIL"  # City is not part of any group
    
    if len(visited) != len(groups):
        return "FAIL"  # Not all groups were visited

    # Checking the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        start = city_coordinates[tour[i]]
        end = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(*start, *end)

    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Define city coordinates and groups based on the problem statement
city_coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
    (62, 26), (79, 31), (61, 90), (42, 49)
]
groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]

# Proposed solution: Tour and Cost
proposed_tour = [0, 5, 6, 7, 0]
proposed_cost = 72.83

# Verify the proposed solution
result = verify_solution(proposed_tour, proposed_cost, groups, city_coordinates)
print(result)