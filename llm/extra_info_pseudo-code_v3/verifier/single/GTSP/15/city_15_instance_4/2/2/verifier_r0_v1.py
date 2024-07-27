import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, city_coordinates, city_groups, expected_cost):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check each city visited from each group exactly once
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the starting and ending depot city 0
        found_group = False
        for index, group in enumerate(city_groups):
            if city in group:
                if index in visited_groups:
                    return "FAIL"
                visited_groups.add(index)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check the total travel cost calculation
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# City coordinates mapping from city index
city_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Provided tour and cost
tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
total_travel_cost = 156.55750207016007

# Verification
result = verify_tour(tour, city_coordinates, city_groups, total_travel_cost)
print(result)  # Output the verification result