import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, city_positions, groups):
    # Check start and end city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check visiting one city from each group
    visited_groups = {0: False, 1: False, 2: False}
    for city in tour[1:-1]:  # exclude the depot city at start and end
        for index, group in enumerate(groups):
            if city in group:
                if visited_groups[index]:
                    return "FAIL"
                visited_groups[index] = True
    
    if not all(visited_groups.values()):
        return "FAIL"
    
    # Calculate and check the total travel cost
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])

    expected_distance = 110.09
    if not math.isclose(total_distance, expected_distance, abs_tol=1e-2):
        return "FAIL"
  
    return "CORRECT"

# City positions (indexed by city number)
city_positions = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Provided tour and claimed total travel cost
tour = [0, 1, 8, 4, 0]
claimed_cost = 110.09  # This value is used just for reporting, actual verification is against calcuated total_distance

# Verify the solution
result = verify_tour(tour, city_positions, groups)
print(result)