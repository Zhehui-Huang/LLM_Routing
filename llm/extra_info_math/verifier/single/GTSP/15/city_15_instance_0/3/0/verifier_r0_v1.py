import math

# Definition of cities with their coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# City groups based on the problem description
city_groups = [
    [2, 7, 10, 11, 14], 
    [1, 3, 5, 8, 13], 
    [4, 6, 9, 12]
]

# Provided sample tour and the associated total travel cost
provided_tour = [0, 8, 0, 8, 0]
provided_total_cost = 78.89

# Function to calculate Euclidean distance between two cities
def euclidean_distance(ci, cj):
    x1, y1 = cities[ci]
    x2, y2 = cities[cj]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Unit test to verify the provided solution against problem requirements
def verify_solution(tour, total_cost):
    # Requirement 1: The robot must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot needs to visit exactly one city from each city group.
    visited_groups = set()
    for idx in tour[1:-1]:  # ignore the depot city at start and end
        for group_idx, group in enumerate(city_groups):
            if idx in group and group_idx not in visited_groups:
                visited_groups.add(group_ph)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Calculate the preserved minimum total travel cost, checks with some error tolerance
    calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if abs(calculated_cost - total_cost) > 1e-2:
        return "FAIL"
    
    return "CORRECT"

# Execute unit test
print(verify_solution(provided_tour, provided_total_cost))