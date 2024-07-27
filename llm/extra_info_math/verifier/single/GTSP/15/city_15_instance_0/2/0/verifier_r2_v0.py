def verify_solution(tour, total_travel_cost):
    # Coordinates of cities
    coordinates = [
        (9, 93),  # Depot city 0
        (8, 51),  # Group 1 city 1
        (74, 99), # Group 0 city 2
        (78, 50), # Group 1 city 3
        (21, 23), # Group 2 city 4
        (88, 59), # Group 1 city 5
        (79, 77), # Group 2 city 6
        (63, 23), # Group 0 city 7
        (19, 76), # Group 1 city 8
        (21, 38), # Group 2 city 9
        (19, 65), # Group 0 city 10
        (11, 40), # Group 0 city 11
        (3, 21),  # Group 2 city 12
        (60, 55), # Group 1 city 13
        (4, 39)   # Group 0 city 14
    ]
    groups = {
        0: [2, 7, 10, 11, 14],
        1: [1, 3, 5, 8, 13],
        2: [4, 6, 9, 12]
    }

    # Check Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return 'FAIL'

    # Check Requirement 2: Visit exactly one city from each group
    visited_groups = {0: False, 1: False, 2: False}
    for city in tour[1:-1]:
        for group, cities in groups.items():
            if city in cities:
                if visited_groups[group]:
                    return 'FAIL'  # Already visited a city from this group
                visited_groups[group] = True
    if not all(visited_groups.values()):
        return 'FAIL'

    # Function to calculate Euclidean distance
    def euclidean_distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    # Check Requirement 3: Minimize the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return 'FAIL'

    return 'CORRECT'

# Provided solution output
tour = [0, 8, 0, 8, 0]
total_travel_cost = 78.89233169326408

# Verify the solution
print(verify_solution(tour, total_credit_cost))