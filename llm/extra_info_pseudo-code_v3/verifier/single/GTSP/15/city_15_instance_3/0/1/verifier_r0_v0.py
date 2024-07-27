import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_tour(tour, city_coordinates, city_groups):
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: One city from each group
    visited_groups = set()
    unique_cities = set(tour)
    
    for city in tour:
        for group_idx, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(group_idx)

    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check Requirement 3: Travel cost via Euclidean distance
    calculated_total_travel_cost = 0
    for i in range(1, len(tour)):
        calculated_total_travel_cost += euclidean_distance(city_coordinates[tour[i - 1]], city_coordinates[tour[i]])

    expected_travel_cost = 138.6273124179014
    if not math.isclose(calculated_total_travel_cost, expected_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities (index of list corresponds to city number)
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Grouping of the cities
city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Proposed solution tour
proposed_tour = [0, 14, 5, 9, 8, 10, 4, 0]

# Output verification result
print(verify_tour(proposed_tour, city_coordinates, city_groups))