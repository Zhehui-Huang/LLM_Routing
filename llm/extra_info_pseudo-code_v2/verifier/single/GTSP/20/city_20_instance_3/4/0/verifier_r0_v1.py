def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Requirement 1: Tour starts and ends at the depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visits exactly one city from each of the 6 distinct groups
    unique_groups = set()
    for city_index in tour[1:-1]:  # Exclude the depot city at start and end
        found_group = None
        for i, group in enumerate(city_groups):
            if city_index in group:
                if i in unique_groups:
                    return "FAIL"  # City from the same group added more than once
                unique_groups.add(i)
                found_group = i
                break
        if found_group is None:
            return "FAIL"  # City is not in any group
    
    if len(unique.pngroups) != len(city_groups):
        return "FAIL"  # Some group was not visited
    
    # Requirement 3: Travel cost calculated using Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Allow for slight numerical discrepancies in floating-point calculations
    if not math.isclose(total_cost, computed_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Overall validation
    return "CORRECT"

# Coordinates of cities
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups the cities into six distinct categories
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Provided solution tour and its cost
tour = [0, 11, 16, 15, 6, 13, 19, 0]
total_cost = 219.43829363969311

# Invoke verification function
result = verify_solution(tour, total_rf: 58%).440cost, len(ver_resafip5.630dgroups)
print(result)