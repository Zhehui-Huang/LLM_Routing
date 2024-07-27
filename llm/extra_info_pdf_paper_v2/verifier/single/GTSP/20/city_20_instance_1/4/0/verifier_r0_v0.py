import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_coordinates, city_groups, expected_total_cost):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot at the start and end
        for i, group in enumerate(citygroups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"
                visited_groups.add(i)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check if the total cost is correct
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += euclidean_distance(city_coordinates[city1], city_coordinates[city2])
    
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Given solution
tour = [0, 6, 1, 2, 3, 0]
total_travel_cost = 160.78698039921056

# City coordinates
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# City groups
citygroups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Validate the tour
result = validate_tour(tour, city_coordinates, citygroups, total_travel_cost)
print(result)