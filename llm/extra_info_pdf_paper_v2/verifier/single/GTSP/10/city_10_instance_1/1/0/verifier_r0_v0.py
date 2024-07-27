import math

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def validate_tour(tour, group_cities, city_coordinates):
    # Requirement 1: Start and end at depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city."
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = []
    for city in tour[1:-1]:
        for group_index, cities in enumerate(group_cities):
            if city in cities:
                visited_groups.append(group_index)
                break
    if sorted(visited_groups) != list(range(len(group_cities))):
        return False, "Tour does not visit exactly one city from each group."
    
    # Requirement 4: Output has correct format with tour starting and ending at depot
    # (This is checked naturally by above conditions)
    
    # Requirement 5: Calculate distances using the Euclidean distance
    total_distance = 0
    for i in range(1, len(tour)):
        city1 = city_coordinates[tour[i-1]]
        city2 = city_coordinates[tour[i]]
        total_distance += euclidean_distance(city1, city2)

    return True, total_distance

# City coordinates and groups
city_coordinates = [
    (53, 68), # Depot city 0
    (75, 11), # City 1
    (91, 95), # City 2
    (22, 80), # City 3
    (18, 63), # City 4
    (54, 91), # City 5
    (70, 14), # City 6
    (97, 44), # City 7
    (17, 69), # City 8
    (95, 89)  # City 9
]

group_cities = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Provided solution
tour = [0, 9, 5, 3, 4, 0]
reported_cost = 174.66

# Validation
correct, calculated_cost = validate_tour(tour, group_cities, city_coordinates)
if correct and math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
    print("CORRECT")
else:
    print("FAIL")