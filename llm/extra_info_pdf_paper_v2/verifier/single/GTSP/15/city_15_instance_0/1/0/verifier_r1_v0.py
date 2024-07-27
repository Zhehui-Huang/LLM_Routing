import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_tour(tour, city_positions, city_groups):
    # Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = {}
    for city in tour:
        for index, group in enumerate(city_groups):
            if city in group:
                if index in visited_groups:
                    return "FAIL"
                visited_groups[index] = True
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculating the total travel distance using the Euclidean distance formula
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])

    expected_distance = 122.21527940040238
    if not math.isclose(total_distance, expected_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Positions of cities by index
city_positions = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Grouping of cities
city_groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]        # Group 2
]

# Solution Tour
solution_tour = [0, 10, 1, 9, 0]

# Verify the solution
result = verify_tour(solution_tour, city_positions, city_groups)
print(result)