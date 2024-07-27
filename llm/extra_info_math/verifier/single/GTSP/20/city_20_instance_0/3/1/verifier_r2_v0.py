def compute_euclidean_distance(coord1, coord2):
    from math import sqrt
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def check_solution(tour, city_coordinates, groups):
    # Check if tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly one city from each group
    visited_groups = [0] * len(groups)  # Tracks which groups have been visited
    for city in tour[1:-1]:  # Exclude the depot city in the beginning and end
        found = False
        for group_index, group_cities in enumerate(groups):
            if city in group_cities:
                if visited_groups[group_index] == 1:
                    return "FAIL"  # A city in this group has already been visited
                visited_groups[group_index] = 1
                found = True
                break
        if not found:
            return "FAIL"  # City is not found in any group
    
    if any(visited == 0 for visited in visited_groups):
        return "FAIL"  # Not all groups are visited exactly once
    
    # Calculate total travel cost from the tour and verify minimization is necessary
    total_computed_distance = 0
    for i in range(len(tour) - 1):
        total_computed_distance += compute_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    reported_distance = 647.765389628066  # As stated in the provided solution
    if abs(total_computed_distance - reported_distance) > 1e-5:
        return "FAIL"  # The reported distance does not match computed

    # If all checks are passed, return CORRECT
    return "CORRECT"

# Define the city coordinates based on the task description
city_coords = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
               (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Define city groups
city_groups = [[1, 3, 5, 11, 13, 14, 19], [2, 6, 7, 8, 12, 15], [4, 9, 10, 16, 17, 18]]

# Provided solution tour
tour = [0, 1, 2, 5, 3, 4, 0, 1, 6, 0, 1, 7, 0, 1, 8, 0, 1, 9, 0, 19, 0]  # This seems incorrect

# Validate the solution
validation_result = check_solution(tour, city_coords, city_groups)
print(validation_result)