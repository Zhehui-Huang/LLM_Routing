import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def validate_tour(tour, city_groups, city_locations):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if it visits exactly one city from each group
    visited_cities = tour[1:-1]  # Exclude depot
    visited_groups = set()
    for city in visited_cities:
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)

    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate distance and compare with reported
    total_distance_calculated = 0
    for i in range(len(tour) - 1):
        total_distance_calculated += calculate_distance(city_locations[tour[i]], city_locations[tour[i + 1]])

    # Checking provided tour distance
    if abs(total_distance_calculated - 324.1817486177585) > 1e-6:
        return "FAIL"

    return "CORRECT"

# City locations and groups
cities_locations = [
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

city_groups = [
    [7, 9],    # Group 0
    [1, 3],    # Group 1
    [4, 6],    # Group 2
    [8],       # Group 3
    [5],       # Group 4
    [2]        # Group 5
]

# Provided solution
tour = [0, 7, 1, 4, 8, 5, 2, 0]
tour_cost = 324.1817486177585

# Validate the solution
result = validate_tour(tour, city_groups, cities_locations)
print(result)