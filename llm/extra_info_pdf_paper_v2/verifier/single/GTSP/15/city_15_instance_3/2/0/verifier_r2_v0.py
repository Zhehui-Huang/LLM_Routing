import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates, city_groups):
    # Verify tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Extract visited cities from the tour (excluding the initial and final depot city)
    visited_cities = tour[1:-1]

    # Verify that exactly one city from each group is visited
    visited_from_groups = set()
    for city in visited_cities:
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_from_groups:
                    return "FAIL"
                visited_from_groups.add(group433_index)
    
    if len(visited_from_groups) != len(city_groups):
        return "FAIL"

    # Verify travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-09):
        return "FAIL"

    return "CORRECT"

# Define city coordinates and city groups
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Tour and total cost
tour = [0, 12, 11, 8, 10, 9, 14, 0]
total_travel_cost = 214.92

# Run verification
result = verify_solution(tour, total_travel_cost, city_coordinates, city_groups)
print(result)